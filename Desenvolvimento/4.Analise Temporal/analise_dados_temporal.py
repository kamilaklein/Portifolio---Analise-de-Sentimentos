import pandas as pd

comentarios_df = pd.read_csv("comentarios.csv")
videos_df = pd.read_csv("videos.csv")

comentarios_df['published_at'] = pd.to_datetime(comentarios_df['published_at'], errors='coerce')

comentarios_df = comentarios_df.dropna(subset=['published_at'])

comentarios_df['mes_ano'] = comentarios_df['published_at'].dt.to_period('M')

comentarios_videos_df = comentarios_df.merge(videos_df, on='video_id', how='left')

comentarios_por_tema_mes = comentarios_videos_df.groupby(['mes_ano', 'video_title']).size().reset_index(name='quantidade')

comentarios_por_tema_mes.to_csv("comentarios_por_tema_mes.csv", index=False)

print("Análise temporal por tema concluída e salva em 'comentarios_por_tema_mes.csv'")
