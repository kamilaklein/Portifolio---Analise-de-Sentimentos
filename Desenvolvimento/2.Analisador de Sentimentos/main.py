import time
import banco_de_dados
import preprocessar_texto
import analise_de_sentimentos
import pandas as pd
from psycopg2 import Error

def atualizar_analises_lote(conn, cursor, df):
    try:
        dados = [(
            row['emotion'],
            row['polarity'],
            row['comment_id']
        ) for _, row in df.iterrows()]
        
        cursor.executemany('''
            UPDATE comentarios 
            SET emotion = %s, polarity = %s 
            WHERE comment_id = %s
        ''', dados)
        
        conn.commit()
        print(f"Análises atualizadas em lote: {len(dados)} registros")
    except Error as e:
        print(f"Erro ao atualizar análises em lote: {e}")
        conn.rollback()

def processar_em_lotes(df, tamanho_lote=1000):
    """Processa o DataFrame em lotes para evitar sobrecarga de memória"""
    return [df[i:i + tamanho_lote] for i in range(0, len(df), tamanho_lote)]

def main():
    tempo_inicio = time.time()
    
    try:
        conn = banco_de_dados.conectar_banco()
        if not conn:
            print("Erro ao conectar ao banco de dados")
            return
        
        cursor = conn.cursor()

        
        print("Carregando dados do banco...")
        comentarios_df = banco_de_dados.carregar_dados(conn)
        
        if comentarios_df.empty:
            print("Nenhum comentário encontrado para análise")
            return

        print(f"Total de comentários carregados: {len(comentarios_df)}")

        print("Filtrando comentários em português...")
        comentarios_df = comentarios_df[
            comentarios_df['comment'].apply(
                lambda x: preprocessar_texto.filtrar_por_idioma(str(x), 'pt')
                if pd.notnull(x) else False
            )
        ]
        
        print(f"Comentários em português: {len(comentarios_df)}")

        print("Realizando análise de sentimentos...")
        comentarios_df = analise_de_sentimentos.analisar_polaridade_sentencas_batch(comentarios_df)
        comentarios_df = analise_de_sentimentos.analisar_emocoes_sentencas_batch(comentarios_df)

        print("Atualizando banco de dados...")
        lotes = processar_em_lotes(comentarios_df, tamanho_lote=1000)
        
        for i, lote in enumerate(lotes, 1):
            print(f"Processando lote {i} de {len(lotes)}...")
            atualizar_analises_lote(conn, cursor, lote)

        print("Salvando resultados completos em CSV...")
        comentarios_df[['comment', 'emotion', 'polarity']].to_csv(
            "resultados_analise_emocoes_polaridade.csv", 
            index=False,
            encoding='utf-8'
        )

        tempo_total = time.time() - tempo_inicio
        print(f"Análise concluída em {tempo_total:.2f} segundos.")
        print(f"Total de comentários analisados: {len(comentarios_df)}")

    except Exception as e:
        print(f"Erro durante a execução: {e}")
    
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
            print("Conexão com o banco fechada.")

if __name__ == "__main__":
    main()