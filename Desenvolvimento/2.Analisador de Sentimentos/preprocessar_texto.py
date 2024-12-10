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
        return detect(texto) == idioma
    except:
        return False
