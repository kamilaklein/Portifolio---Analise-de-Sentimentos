import re
from langdetect import detect

def preprocessar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r'http\S+|www\S+|https\S+', '', texto, flags=re.MULTILINE)
    texto = re.sub(r'\W', ' ', texto)
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto

def filtrar_por_idioma(texto, idioma='pt'):
    try:
        detected_idioma = detect(texto)
        print(f"Idioma detectado: {detected_idioma}")
        return detected_idioma == idioma
    except Exception as e:
        print(f"Erro na detecção de idioma: {e}")
        return False

texto_original = "Adorei essa vela!"
texto_limpo = preprocessar_texto(texto_original)

print("Original:", filtrar_por_idioma(texto_original, idioma='pt'))
print("Pré-processado:", filtrar_por_idioma(texto_limpo, idioma='pt'))

