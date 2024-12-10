import pandas as pd
import re
from wordcloud import WordCloud  # Importando do módulo oficial `wordcloud`
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download('stopwords')
nltk.download('punkt')

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
    
    # Recria o texto processado
    return " ".join(tokens)

texto_processado = preprocessar_texto_wordcloudy(texto)

# Gera a WordCloud
wordcloud = WordCloud(width=800, height=400, background_color='white', max_words=100, colormap='viridis').generate(texto_processado)

# Configurações para exibição
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
