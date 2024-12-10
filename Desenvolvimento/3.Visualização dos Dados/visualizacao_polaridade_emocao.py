import pandas as pd
import plotly.express as px

comentarios_df = pd.read_csv("resultados_analise_emocoes_polaridade.csv")

cores_polaridade = {
    "positivo": "green",
    "neutro": "blue",
    "negativo": "red"
}

polaridade_counts = comentarios_df['polarity'].value_counts().reset_index()
polaridade_counts.columns = ['Polaridade', 'Contagem']
polaridade_counts['Percentual'] = (polaridade_counts['Contagem'] / polaridade_counts['Contagem'].sum()) * 100

fig_polaridade = px.bar(polaridade_counts, 
                        x='Polaridade', y='Percentual',
                        title='Distribuição de polaridade dos comentários',
                        color='Polaridade',
                        color_discrete_map=cores_polaridade,
                        text='Percentual', 
                        hover_data={'Contagem': True, 'Percentual': ':.2f'})  

fig_polaridade.update_traces(texttemplate='%{text:.2f}%', textposition='outside')

fig_polaridade.show()

cores_emocoes = {
    "neutral": "gray",
    "joy": "green",
    "surprise": "purple",
    "anger": "black",
    "sadness": "navy",
    "disgust": "brown",
    "fear": "orange"
}

emocoes_counts = comentarios_df['emotion'].value_counts().reset_index()
emocoes_counts.columns = ['Emoção', 'Contagem']
emocoes_counts['Percentual'] = (emocoes_counts['Contagem'] / emocoes_counts['Contagem'].sum()) * 100

fig_emocoes = px.bar(emocoes_counts, 
                     x='Emoção', y='Percentual',
                     title='Distribuição de emoções dos comentários',
                     color='Emoção', 
                     color_discrete_map=cores_emocoes,
                     text='Percentual', 
                     hover_data={'Contagem': True, 'Percentual': ':.2f'}) 

fig_emocoes.update_traces(texttemplate='%{text:.2f}%', textposition='outside')

fig_emocoes.show()
