from flask import request
import nltk
import spacy
from nltk.tokenize import word_tokenize
from fuzzywuzzy import fuzz
from nltk.util import ngrams
from models import user
from src import analysis_of_feelings

# Cargar modelos y descargar datos necesarios solo una vez
nlp = spacy.load("es_core_news_sm")
nltk.download('punkt')

# Variables y configuración
User = user.Paciente()
UMBRAL_SIMILITUD = 90
OBJECT_ANALYSIS = analysis_of_feelings.prepare()

# Función que analiza los datos
def analyze_data(data):
    # Tokenización de oraciones
    (phrases, separate_words) = get_text(data)
    filtered_words = []
    filtered_phrases = []
    for campo in User.CAMPOS:
        # Filtrar palabras similares a las opciones de cada campo
        filtered_words.extend( filter_words(separate_words, campo,80))
        # Obtener las palabras más relevantes
        filtered_phrases.extend( filter_words(phrases, campo, 80))
    print(f"Palabras similares: {filtered_words}")
    print(f"Frases similares: {filtered_phrases}")


    # Análisis de palabras solas
    for word in filtered_words:
        contexto = get_word_context(data, word)
        print(f"Contexto de la palabra '{word}': {contexto}")

    return User

def get_text(text):
    # Tokenización y procesamiento de spaCy
    doc = nlp(text)

    # Crear listas para almacenar frases y palabras separadas
    phrases = []
    separate_words = set()  # Usar un conjunto para palabras únicas

    # Extraer entidades nombradas
    for entity in doc.ents:
        phrases.append(entity.text)

    # Tokenizar y obtener palabras no incluidas en las frases (palabras separadas)
    tokens = [token.text for token in doc if not token.is_stop and not token.is_punct and token.text not in phrases]

    # Generar n-grams
    bigrams = [' '.join(bigram) for bigram in ngrams(tokens, 2)]
    trigrams = [' '.join(trigram) for trigram in ngrams(tokens, 3)]

    # Añadir n-grams a frases
    phrases.extend(bigrams)
    phrases.extend(trigrams)

    # Separar palabras únicas no agrupadas
    for token in tokens:
        separate_words.add(token)

    return (phrases, list(separate_words))  # Convertir de nuevo a lista


def filter_words(words, target_word, threshold=UMBRAL_SIMILITUD):
    # Filtrar palabras similares a la palabra objetivo
    return [word for word in words if fuzz.partial_ratio(word.lower(), target_word.lower()) >= threshold]


def get_word_context(text, target_word, context_words=3):
    # Tokenizar el texto en palabras
    words = word_tokenize(text)
    
    # Encontrar los índices de la palabra objetivo
    target_indices = [i for i, word in enumerate(words) if word.lower() == target_word.lower()]
    
    contexts = []
    
    for index in target_indices:
        # Calcular los índices de inicio y fin para el contexto
        start_index = max(0, index - context_words)
        end_index = min(len(words), index + context_words + 1)  # +1 para incluir la palabra objetivo
        
        # Extraer el contexto
        context = words[start_index:end_index]
        contexts.append(' '.join(context))  # Agregar el contexto como una cadena

    return ' | '.join(contexts)  # Devolver todos los contextos separados por ' | '

# Resto de tu código permanece igual
