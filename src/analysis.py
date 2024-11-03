import nltk
import os
import spacy

from nltk.tokenize import sent_tokenize

nlp = spacy.load("es_core_news_sm")
nltk.download('punkt_tab')

# Función que analiza los datos
def analyze_data(data):
    # Tokenización de oraciones
    oraciones = sent_tokenize(data)

    for oracion in oraciones:
        # Procesamiento con spaCy
        doc = nlp(oracion)
        
            


    return ";("






