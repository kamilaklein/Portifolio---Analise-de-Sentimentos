import time
import csv
from googleapiclient.discovery import build
from langdetect import detect
import psycopg2
from psycopg2 import Error
from datetime import datetime
from contextlib import contextmanager

DB_CONFIG = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

YOUTUBE_API_KEY = 'AIzaSyCYB0jcYh16SmW3pY-tCPaJbNKPYEnuGj4'
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
search_terms = [
    "velas aromáticas",
    "velas decorativas",
    "como fazer velas aromáticas",
    "artesanato com velas",
    "decoração com velas"
]

@contextmanager
def get_cursor(conn):
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()

def initialize_database(conn):
    with get_cursor(conn) as cursor:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS videos (
                video_id TEXT PRIMARY KEY,
                video_title TEXT,
                video_description TEXT,
                published_at TIMESTAMP,
                view_count INTEGER,
                like_count INTEGER,
                comment_count INTEGER
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS comentarios (
                comment_id TEXT PRIMARY KEY,
                video_id TEXT REFERENCES videos (video_id),
                username TEXT,
                comment TEXT,
                like_count INTEGER,
                published_at TIMESTAMP
            )
        ''')

def save_video(conn, video_data):
    with get_cursor(conn) as cursor:
        cursor.execute('''
            INSERT INTO videos (video_id, video_title, video_description, published_at, view_count, like_count, comment_count)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (video_id) DO UPDATE SET
                video_title = EXCLUDED.video_title,
                video_description = EXCLUDED.video_description,
                published_at = EXCLUDED.published_at,
                view_count = EXCLUDED.view_count,
                like_count = EXCLUDED.like_count,
                comment_count = EXCLUDED.comment_count
        ''', video_data)
        return True

def save_comment(conn, comment_data):
    with get_cursor(conn) as cursor:
        cursor.execute('''
            INSERT INTO comentarios (comment_id, video_id, username, comment, like_count, published_at)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (comment_id) DO UPDATE SET
                username = EXCLUDED.username,
                comment = EXCLUDED.comment,
                like_count = EXCLUDED.like_count,
                published_at = EXCLUDED.published_at
        ''', comment_data)
        return True

def process_comments(conn, video_id, comentarios_writer):
    next_page_token = None
    while True:
        try:
            comments_response = youtube.commentThreads().list(
                videoId=video_id,
                part='snippet',
                maxResults=100,
                pageToken=next_page_token 
            ).execute()
            
            for comment_item in comments_response['items']:
                try:
                    comment = comment_item['snippet']['topLevelComment']['snippet']
                    comment_id = comment_item['id']
                    username = comment['authorDisplayName']
                    comment_text = comment['textDisplay']
                    like_count = int(comment['likeCount'])
                    comment_published_at = comment['publishedAt']
                    
                    try:
                        if detect(comment_text) == 'pt':
                            comment_data = (comment_id, video_id, username, 
                                          comment_text, like_count, comment_published_at)
                            
                            if save_comment(conn, comment_data):
                                comentarios_writer.writerow(list(comment_data))
                                print(f'{username} => {comment_text}')
                    except Exception as lang_error:
                        print(f"Erro ao detectar idioma para o comentário {comment_id}: {lang_error}")
                        continue
                        
                except Exception as comment_error:
                    print(f"Erro ao processar comentário: {comment_error}")
                    continue
    
            next_page_token = comments_response.get('nextPageToken')
            if not next_page_token:
                break
            
            time.sleep(2)
            
        except Exception as e:
            print(f"Erro ao coletar comentários do vídeo {video_id}: {e}")
            break

def main():
    try:
        conn = psycopg2.connect(**DB_CONFIG)

        initialize_database(conn)

        with open('videos.csv', mode='w', newline='', encoding='utf-8') as videos_csv, \
             open('comentarios.csv', mode='w', newline='', encoding='utf-8') as comentarios_csv:
            
            videos_writer = csv.writer(videos_csv)
            comentarios_writer = csv.writer(comentarios_csv)
            
            videos_writer.writerow(['video_id', 'video_title', 'video_description', 'published_at', 'view_count', 'like_count', 'comment_count'])
            comentarios_writer.writerow(['comment_id', 'video_id', 'username', 'comment', 'like_count', 'published_at'])

            search_response = youtube.search().list(
                q=search_terms,
                part='id,snippet',
                type='video',
                maxResults=30 
            ).execute()

            for item in search_response['items']:
                try:
                    video_id = item['id']['videoId']
                    
                    video_details = youtube.videos().list(
                        id=video_id,
                        part='snippet,statistics'
                    ).execute()
                    
                    video_info = video_details['items'][0]
                    video_title = video_info['snippet']['title']
                    video_description = video_info['snippet'].get('description', 'Sem descrição')
                    published_at = video_info['snippet']['publishedAt']
                    view_count = int(video_info['statistics'].get('viewCount', 0))
                    like_count = int(video_info['statistics'].get('likeCount', 0))
                    comment_count = int(video_info['statistics'].get('commentCount', 0))
                    
                    print(f"\nSalvando informações do vídeo: {video_title} (ID: {video_id})")

                    video_data = (video_id, video_title, video_description, published_at, 
                                view_count, like_count, comment_count)
                    
                    if save_video(conn, video_data):
                        videos_writer.writerow(list(video_data))
                        process_comments(conn, video_id, comentarios_writer)
                
                except Exception as video_error:
                    print(f"Erro ao processar vídeo: {video_error}")
                    continue

    except (Exception, Error) as error:
        print(f"Erro ao conectar ao PostgreSQL: {error}")

    finally:
        if conn:
            conn.close()
            print("Conexão com PostgreSQL fechada.")
            
    print("Coleta de dados concluída. Os dados foram salvos no banco de dados PostgreSQL e nos arquivos CSV.")

if __name__ == "__main__":
    main()