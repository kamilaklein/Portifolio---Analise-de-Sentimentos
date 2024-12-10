import pandas as pd
import plotly.express as px
import re

comentarios_por_tema_mes = pd.read_csv("comentarios_por_tema_mes.csv")

comentarios_por_tema_mes['mes_ano'] = pd.to_datetime(comentarios_por_tema_mes['mes_ano'], format='%Y-%m')

total_comentarios_por_tema = comentarios_por_tema_mes.groupby('video_title')['quantidade'].sum()

principais_temas = total_comentarios_por_tema.nlargest(10).index

comentarios_top_temas = comentarios_por_tema_mes[comentarios_por_tema_mes['video_title'].isin(principais_temas)]

comentarios_top_temas['video_title'] = comentarios_top_temas['video_title'].apply(lambda x: re.sub(r'[^\x00-\x7F]+', '', x))

fig = px.line(comentarios_top_temas,
              x='mes_ano', y='quantidade', color='video_title',
              title="Número de comentários por mês para os principais temas:",
              labels={'mes_ano': 'Mês', 'quantidade': 'Número de comentários', 'video_title': 'Tema do vídeo'})

fig.show()
