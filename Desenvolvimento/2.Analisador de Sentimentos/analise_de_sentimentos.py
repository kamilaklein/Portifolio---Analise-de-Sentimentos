from transformers import pipeline
from nltk.tokenize import sent_tokenize
import pandas as pd
from preprocessar_texto import preprocessar_texto

def mapear_polaridade(label):
    if label in ["5 stars", "4 stars"]:
        return "positivo"
    elif label == "3 stars" or label in ["neutral", "indifference"]:
        return "neutro"
    else:
        return "negativo"

def ajustar_neutralidade(comentarios_df):
    neutras = ["qual", "como", "onde", "quando", "será", "pode", "misturar"]
    for index, row in comentarios_df.iterrows():
        if any(palavra in row['comment'].lower() for palavra in neutras):
            comentarios_df.at[index, 'polarity'] = "neutro"
    return comentarios_df

def identificar_perguntas(comentario):
    return "neutro" if comentario.strip().endswith("?") else None

def analisar_polaridade_sentencas_batch(comentarios_df, batch_size=16, max_chunk_size=512):
    sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
    polaridades = []
    
    comentarios = comentarios_df['comment'].tolist()
    for i in range(0, len(comentarios), batch_size):
        batch = comentarios[i:i + batch_size]
        
        chunks = []
        for comment in batch:
            palavras = comment.split()
            chunks.extend([" ".join(palavras[j:j + max_chunk_size]) for j in range(0, len(palavras), max_chunk_size)])
        
        results = sentiment_pipeline(chunks, truncation=True)
        
        for comment in batch:
            chunks_for_comment = [result['label'] for result in results[:len(comment.split()) // max_chunk_size + 1]]
            results = results[len(chunks_for_comment):]  # Remove os chunks processados
            polaridades_chunks = [mapear_polaridade(label) for label in chunks_for_comment]
            polaridade_final = pd.Series(polaridades_chunks).value_counts().idxmax()
            polaridades.append(polaridade_final)
    
    comentarios_df['polarity'] = polaridades
    return comentarios_df

def analisar_emocoes_sentencas_batch(comentarios_df, batch_size=16, max_chunk_size=512):
    emotion_pipeline = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)
    emotions = []
    
    comentarios = comentarios_df['comment'].tolist()
    for i in range(0, len(comentarios), batch_size):
        batch = comentarios[i:i + batch_size]
        
        chunks = []
        chunk_map = []
        for idx, comment in enumerate(batch):
            palavras = comment.split()
            comment_chunks = [" ".join(palavras[j:j + max_chunk_size]) for j in range(0, len(palavras), max_chunk_size)]
            chunks.extend(comment_chunks)
            chunk_map.extend([idx] * len(comment_chunks))
        
        results = emotion_pipeline(chunks, truncation=True)
        
        batch_emotions = [""] * len(batch)
        for idx in range(len(batch)):
            comment_results = [results[j] for j, m in enumerate(chunk_map) if m == idx]
            sentenca_emocoes = [result[0]['label'] for result in comment_results]
            emotion_count = pd.Series(sentenca_emocoes).value_counts()
            emotion_principal = emotion_count.idxmax()
            batch_emotions[idx] = emotion_principal
        
        emotions.extend(batch_emotions)
    
    comentarios_df['emotion'] = emotions
    return comentarios_df 
