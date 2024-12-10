import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

file_path = 'C:/Users/kamil/OneDrive/Área de Trabalho/Kamila/Faculdade Kamila/Analisador de Sentimento/Projeto Analise de Sentimentos/5.Testes/comentarios_analisepolaridade_testes.csv'

try:
    data = pd.read_csv(file_path, on_bad_lines='skip')

    cleaned_data = data.dropna(subset=['polarity', 'predicted_polarity']).copy()

    cleaned_data['polarity'] = cleaned_data['polarity'].astype(str)
    cleaned_data['predicted_polarity'] = cleaned_data['predicted_polarity'].astype(str)

    y_true = cleaned_data['predicted_polarity']
    y_pred = cleaned_data['polarity']

    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='weighted', zero_division=0)
    recall = recall_score(y_true, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_true, y_pred, average='weighted', zero_division=0)


    print(f"Acuracidade: {accuracy:.2%}")
    print(f"Precisão (Precision): {precision:.2%}")
    print(f"Revocação (Recall): {recall:.2%}")
    print(f"F1-Score: {f1:.2%}")

except FileNotFoundError:
    print(f"Erro: O arquivo {file_path} não foi encontrado.")
except Exception as e:
    print(f"Erro ao processar o arquivo: {e}")
