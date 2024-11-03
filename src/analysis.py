import nltk
import os
nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize

# Función que analiza los datos
def analyze_data(data):
    # Tokenización de oraciones
    oraciones = sent_tokenize(data)
    return oraciones






