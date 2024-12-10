import sqlite3
import pandas as pd
import nltk
from nltk.corpus import stopwords
from collections import Counter
import re
#from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('comentarios_youtube.db')

# Carregar dados da tabela videos para um DataFrame
videos_df = pd.read_sql_query("SELECT * FROM videos", conn)

# Fechar a conexão
conn.close()

# Certifique-se de ter baixado as stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('portuguese'))  # Stop words em português

# Lista de materiais comuns para velas aromáticas
common_materials = ["cera", "soja", "abelha", "parafina", "pavio", "essência", "óleo", 
                    "essencial", "aroma", "frasco", "corante", "recipiente", "copos"]

# Função para pré-processar o texto, com foco em materiais
def preprocess_text(text):
    # Remover URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    # Remover caracteres especiais e números, deixando apenas letras
    text = re.sub(r'[^a-zA-ZáéíóúãõâêôçÁÉÍÓÚÃÕÂÊÔÇ ]', ' ', text.lower())
    # Tokenizar e remover stop words, mantendo materiais na lista de interesse
    tokens = [word for word in text.split() if word not in stop_words and (len(word) > 2 or word in common_materials)]
    return tokens

# 1. Análise de Palavras Frequentes com Foco em Materiais
def analyze_word_frequency(dataframe):
    # Combinar todas as descrições em um único texto e pré-processá-lo
    text_data = ' '.join(dataframe['video_description'].fillna(''))
    tokens = preprocess_text(text_data)
    
    # Contar as palavras mais frequentes, dando prioridade aos materiais comuns
    material_counts = Counter([word for word in tokens if word in common_materials])
    
    # Exibir os materiais mais comuns
    print("Materiais mais frequentes nas descrições (após pré-processamento):")
    for material, freq in material_counts.most_common(20):
        print(f"{material}: {freq}")
    
    # Gerar e exibir uma nuvem de palavras para materiais
    #wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(dict(material_counts))
    plt.figure(figsize=(10, 5))
   # plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Nuvem de Palavras (Materiais nas Descrições)")
    plt.show()


# 2. Correlação entre Visualizações e Técnicas (com Pré-processamento)
def analyze_views_correlation(dataframe):
    # Definir as técnicas de interesse, com pré-processamento nos dados
    techniques = ['fácil', 'diy', 'cera de coco', 'produção']
    
    for technique in techniques:
        # Filtrar vídeos que mencionam a técnica apenas na descrição
        dataframe['processed_description'] = dataframe['video_description'].apply(preprocess_text)
        technique_videos = dataframe[dataframe['processed_description'].apply(lambda x: technique in x)]
        
        avg_views = technique_videos['view_count'].mean()
        print(f"Média de visualizações para vídeos com '{technique}' na descrição (após pré-processamento): {avg_views}")

# 3. Popularidade e Engajamento
def analyze_popularity_engagement(dataframe):
    techniques = ['fácil', 'diy', 'cera de coco', 'produção']
    
    for technique in techniques:
        # Filtrar vídeos que mencionam a técnica
        technique_videos = dataframe[dataframe['video_description'].str.contains(technique, case=False, na=False) |
                                     dataframe['video_title'].str.contains(technique, case=False, na=False)]
        
        avg_likes = technique_videos['like_count'].mean()
        avg_comments = technique_videos['comment_count'].mean()
        
        print(f"Engajamento para vídeos com '{technique}':\n Curtidas: {avg_likes}\n Comentários: {avg_comments}")

# 4. Análise Temporal
def analyze_temporal_trends(dataframe):
    # Converter a coluna 'published_at' para datetime
    dataframe['published_at'] = pd.to_datetime(dataframe['published_at'])
    
    # Extrair o mês e o ano da data de publicação
    dataframe['year_month'] = dataframe['published_at'].dt.to_period('M')
    
    # Agrupar por mês e ano para ver a média de visualizações, curtidas e comentários
    temporal_data = dataframe.groupby('year_month').agg({'view_count': 'mean', 'like_count': 'mean', 'comment_count': 'mean'})
    
    # Converter o índice para DateTime para compatibilidade com matplotlib
    temporal_data.index = temporal_data.index.to_timestamp()

    # Plotar tendências temporais
    plt.figure(figsize=(10, 6))
    plt.plot(temporal_data['view_count'], label='Média de Visualizações')
    plt.plot(temporal_data['like_count'], label='Média de Curtidas')
    plt.plot(temporal_data['comment_count'], label='Média de Comentários')
    plt.xlabel('Ano-Mês')
    plt.ylabel('Média')
    plt.title("Tendências Temporais de Engajamento e Visualizações")
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()

# Chamar as funções para executar as análises
analyze_word_frequency(videos_df)
analyze_views_correlation(videos_df)
analyze_popularity_engagement(videos_df)
analyze_temporal_trends(videos_df)
