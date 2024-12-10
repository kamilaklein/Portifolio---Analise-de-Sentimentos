import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloudy_analysis import WordCloud
import matplotlib.pyplot as plt
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download('stopwords')
nltk.download('punkt')

def preprocessar_texto(texto):
    import re
from langdetect import detect
from nltk.corpus import stopwords
import spacy
import emoji

nlp = spacy.load("pt_core_news_sm")
stop_words = set(stopwords.words('portuguese'))


comentarios_df = pd.read_csv("comentarios.csv")
texto = " ".join(comentarios_df['comment'].astype(str).tolist())

def preprocessar_texto_wordcloudy(texto):
    texto = texto.lower()
    texto = re.sub(r'http\S+|www\S+', '', texto)
    texto = re.sub(r'\W|\d', ' ', texto)
    texto = re.sub(r'\s+', ' ', texto).strip()
    palavras_para_remover = r'\b(pra|br|q|oi|ficar|ter|assim|pq|o|vc)\b'
    texto = re.sub(palavras_para_remover, '', texto)    
    
    stop_words = set(stopwords.words('portuguese'))
    tokens = word_tokenize(texto)
    tokens = [word for word in tokens if word not in stop_words]
    
    return " ".join(tokens)

texto_processado = preprocessar_texto_wordcloudy(texto)


def filtrar_por_idioma(texto, idioma='pt'):
    try:
        return detect(texto) == idioma
    except:
        return False

def carregar_dados():
    comentarios_df = pd.read_csv("resultados_analise_emocoes_polaridade.csv")
    comentarios_top_temas = pd.read_csv("comentarios_por_tema_mes.csv")
    return comentarios_df, comentarios_top_temas

def mostrar_grafico_polaridade(comentarios_df):
    cores_polaridade = {"positivo": "green", "neutro": "blue", "negativo": "red"}
    polaridade_counts = comentarios_df['polarity'].value_counts().reset_index()
    polaridade_counts.columns = ['Polaridade', 'Contagem']
    polaridade_counts['Percentual'] = (polaridade_counts['Contagem'] / polaridade_counts['Contagem'].sum()) * 100
    fig_polaridade = px.bar(polaridade_counts, x='Polaridade', y='Percentual', title='Distribuição de polaridade dos comentários',
                            color='Polaridade', color_discrete_map=cores_polaridade, text='Percentual', hover_data={'Contagem': True, 'Percentual': ':.2f'})
    fig_polaridade.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
    st.plotly_chart(fig_polaridade)

def mostrar_grafico_emocoes(comentarios_df):
    cores_emocoes = {"neutral": "gray", "joy": "green", "surprise": "purple", "anger": "black", "sadness": "navy", "disgust": "brown", "fear": "orange"}
    emocoes_counts = comentarios_df['emotion'].value_counts().reset_index()
    emocoes_counts.columns = ['Emoção', 'Contagem']
    emocoes_counts['Percentual'] = (emocoes_counts['Contagem'] / emocoes_counts['Contagem'].sum()) * 100
    fig_emocoes = px.bar(emocoes_counts, x='Emoção', y='Percentual', title='Distribuição de emoções dos comentários',
                         color='Emoção', color_discrete_map=cores_emocoes, text='Percentual', hover_data={'Contagem': True, 'Percentual': ':.2f'})
    fig_emocoes.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
    st.plotly_chart(fig_emocoes)

def mostrar_nuvem_palavras(comentarios_df):
    texto = " ".join(comentarios_df['comment'].astype(str).tolist())
    texto_processado = preprocessar_texto_wordcloudy(texto)
    wordcloud = WordCloud(width=800, height=400, background_color='white', max_words=100, colormap='viridis').generate(texto_processado)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot(plt)

def mostrar_analise_temporal(comentarios_top_temas):
    comentarios_top_temas['mes_ano'] = pd.to_datetime(comentarios_top_temas['mes_ano'], format='%Y-%m')
    total_comentarios_por_tema = comentarios_top_temas.groupby('video_title')['quantidade'].sum()
    principais_temas = total_comentarios_por_tema.nlargest(10).index
    comentarios_top_temas = comentarios_top_temas[comentarios_top_temas['video_title'].isin(principais_temas)]
    comentarios_top_temas['video_title'] = comentarios_top_temas['video_title'].apply(lambda x: re.sub(r'[^\x00-\x7F]+', '', x))
    fig = px.line(comentarios_top_temas, x='mes_ano', y='quantidade', color='video_title',
                  title="Número de comentários por mês para os principais temas:",
                  labels={'mes_ano': 'Mês', 'quantidade': 'Número de comentários', 'video_title': 'Tema do vídeo'})
    st.plotly_chart(fig)

st.title("**Análise de sentimentos e emoções dos comentários:**")
st.write("""
    Bem-vindo ao painel de análise de sentimentos e emoções! Aqui você pode explorar diferentes visualizações para entender
    melhor as reações e emoções expressas nos comentários. 
    Use os botões à esquerda para projetar os gráficos:
    
    - **Distribuição de polaridade**: Proporção de comentários positivos, neutros e negativos.
    - **Distribuição de emoções**: Identificar as emoções como alegria, surpresa, tristeza e mais.
    - **Nuvem de palavras**: As palavras mais frequentes nos comentários.
    - **Análise temporal**: Observar a evolução dos comentários ao longo do tempo.
""")

st.sidebar.header("Selecione a análise:")

comentarios_df, comentarios_top_temas = carregar_dados()

if st.sidebar.button("Visualizar polaridade"):
    mostrar_grafico_polaridade(comentarios_df)

if st.sidebar.button("Visualizar emoções"):
    mostrar_grafico_emocoes(comentarios_df)

if st.sidebar.button("Nuvem de palavras"):
    mostrar_nuvem_palavras(comentarios_df)

if st.sidebar.button("Análise temporal"):
    mostrar_analise_temporal(comentarios_top_temas)
