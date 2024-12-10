import pandas as pd
from transformers import pipeline
import re
import emoji
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('portuguese'))

def preprocessar_texto(texto):
    """
    Limpa e normaliza o texto antes da análise.
    """
    texto = emoji.replace_emoji(texto, replace='')
    texto = texto.lower()
    texto = re.sub(r'[^\w\s]', '', texto)
    palavras = word_tokenize(texto)
    palavras = [palavra for palavra in palavras if palavra not in stop_words]
    texto_limpo = ' '.join(palavras)
    return texto_limpo

def identificar_perguntas(comentario):
    """
    Verifica se o comentário é uma pergunta.
    Se for, classifica como 'neutro'.
    """
    palavras_chave = ["como", "o que", "por que", "quando", "onde", "qual", "será"]
    if comentario.strip().endswith("?") or any(palavra in comentario.lower() for palavra in palavras_chave):
        return "neutro"
    return None

def preprocessar_perguntas(df):
    """
    Identifica perguntas e atribui a polaridade como 'neutro' antes da análise.
    """
    for index, row in df.iterrows():
        if identificar_perguntas(row['comment']) == "neutro":
            df.at[index, 'polarity'] = "neutro"
    return df

def map_polarity(label):
    """
    Mapeia os resultados de sentimento do modelo para polaridades.
    """
    if label in ["5 stars", "4 stars"]:
        return "positivo"
    elif label == "3 stars":
        return "neutro"
    else:
        return "negativo"

file_name = 'C:/Users/kamil/OneDrive/Área de Trabalho/Kamila/Faculdade Kamila/Analisador de Sentimento/comentarios.csv'
comments_data = pd.read_csv(file_name)

comments_data['polarity'] = None  
comments_data = preprocessar_perguntas(comments_data)

comentarios_para_analisar = comments_data[comments_data['polarity'].isnull()]

sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

if not comentarios_para_analisar.empty:
    comments = comentarios_para_analisar['comment'].tolist()
    results = sentiment_pipeline(comments, truncation=True)


    polarities = [map_polarity(result['label']) for result in results]
    comments_data.loc[comments_data['polarity'].isnull(), 'polarity'] = polarities


output_file_path = 'comentarios_polaridade_final.csv'
comments_data.to_csv(output_file_path, index=False)

print(f"Análise de polaridade concluída. Resultados salvos em {output_file_path}.")
