import psycopg2
from psycopg2 import Error
import pandas as pd

def conectar_banco():
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            database="postgres",
            user="postgres",
            password="postgres"
        )
        return conn
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def criar_tabela_analise_sentimentos(conn, cursor):
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS analise_sentimentos (
                comment_id SERIAL PRIMARY KEY,
                comment TEXT,
                emotion VARCHAR(255),
                polarity VARCHAR(255)
            );
        ''')
        conn.commit()
        print("Tabela 'analise_sentimentos' criada ou já existe.")
    except Error as e:
        print(f"Erro ao criar tabela 'analise_sentimentos': {e}")
        conn.rollback()

def carregar_dados(conn):
    try:
        query = "SELECT * FROM comentarios;"
        return pd.read_sql_query(query, conn)
    except Error as e:
        print(f"Erro ao carregar dados: {e}")
        return pd.DataFrame()
