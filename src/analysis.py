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
UMBRAL_SIMILITUD = 80
OBJECT_ANALYSIS = analysis_of_feelings.prepare()

def analyze_data(data):
    """ Analiza los datos del paciente para extraer sentimientos y palabras clave. """
    data = data.lower()
    phrases, separate_words = get_text(data)
    
    filtered_words = set()  # Usar un conjunto para palabras únicas
    filtered_phrases = set()

    for campo in User.CAMPOS:
        filtered_words.update(filter_words(separate_words, campo, UMBRAL_SIMILITUD))
        filtered_phrases.update(filter_phrases(phrases, campo))

        for word in User.CAMPOS[campo]['choices']:
            filtered_words.update(filter_words(separate_words, word, UMBRAL_SIMILITUD))
            filtered_phrases.update(filter_phrases(phrases, word))
    print(filtered_words)
    print(filtered_phrases)
    analyze_filtered_words(filtered_words, data)
    analyze_filtered_phrases(filtered_phrases, data)

    return User

def get_text(text):
    """ Tokeniza el texto en frases y palabras, generando bigramas y trigramas. """
    doc = nlp(text)
    phrases = {entity.text for entity in doc.ents}  # Conjunto para frases únicas
    tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]

    # Generar n-grams
    bigrams = {' '.join(bigram) for bigram in ngrams(tokens, 2)}
    trigrams = {' '.join(trigram) for trigram in ngrams(tokens, 3)}

    phrases.update(bigrams)
    phrases.update(trigrams)

    return (list(phrases), list(set(tokens)))  # Convertir a lista para devolver

def filter_words(words, target_word, threshold):
    """ Filtra palabras similares a la palabra objetivo. """
    return [word for word in words if fuzz.partial_ratio(word.lower(), target_word.lower()) >= threshold]

def filter_phrases(phrases, target_word):
    """ Filtra frases que contienen la palabra objetivo. """
    return [phrase for phrase in phrases if fuzz.partial_ratio(target_word, phrase) >= UMBRAL_SIMILITUD]

def analyze_filtered_words(filtered_words, data):
    """ Analiza las palabras filtradas en el contexto del texto. """
    for word in filtered_words:
        contexto = get_word_context(data, word)
        for campo in User.CAMPOS:
            if campo in contexto:
                analyze_feelings(campo, contexto)

def analyze_filtered_phrases(filtered_phrases, data):
    """ Analiza las frases filtradas. """
    for campo in User.CAMPOS:
        for phrase in filtered_phrases:
            if fuzz.partial_ratio(campo.lower(), phrase.lower()) >= UMBRAL_SIMILITUD:
                analyze_feelings(campo, phrase)

def get_word_context(text, target_word, context_words=5):
    """ Obtiene el contexto de una palabra objetivo en el texto. """
    words = word_tokenize(text)
    target_indices = [i for i, word in enumerate(words) if word.lower() == target_word.lower()]
    contexts = []

    for index in target_indices:
        start_index = max(0, index - context_words)
        end_index = min(len(words), index + context_words + 1)  # +1 para incluir la palabra objetivo
        context = words[start_index:end_index]
        contexts.append(' '.join(context))

    return ' | '.join(contexts)

def analyze_feelings(campo, text):
    """ Analiza los sentimientos relacionados con un campo. """
    if campo in ['nodulo', 'microcalcificaciones', 'asimetrias']:
        result = analysis_of_feelings.analyze_feelings(text, OBJECT_ANALYSIS)
        print(result)   
        valor = User.CAMPOS[campo]['choices'][1] if result[0]['label'] > "3 star" else User.CAMPOS[campo]['choices'][0]
        User.set_campo(campo, valor )
    else:
        valor = encontrar_elemento_en_cadena(User.CAMPOS[campo]['choices'], text)
        User.set_campo(campo, valor if valor else "N.A")  # Asignar valor o "N.A."

def encontrar_elemento_en_cadena(lista, cadena):
    """ Encuentra un elemento en la lista que se asemeje a la cadena dada. """
    return next((elemento for elemento in lista if fuzz.partial_ratio(elemento.lower(), cadena.lower()) >= UMBRAL_SIMILITUD), None)
