import unicodedata
import nltk
import spacy
import re
from nltk.tokenize import word_tokenize
from fuzzywuzzy import fuzz
from nltk.util import ngrams
from models import user
from src import analysis_of_feelings
from nltk.tokenize import sent_tokenize

# Cargar modelos y descargar datos necesarios solo una vez
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')

# Load spaCy model
nlp = spacy.load("es_core_news_sm")

# Variables y configuración
User = user.Paciente()
UMBRAL_SIMILITUD = 80
OBJECT_ANALYSIS = analysis_of_feelings.prepare()

def analyze_data(data):
    processed_sentences = process_text(data)
    fist_analysis(processed_sentences)  # Analizar las oraciones procesadas

    print(User.to_dict())
    return User

# Función para procesar el texto
def process_text(text):
    # Corregir el texto
    text = correct_text(text)
    
    # Dividir el texto en oraciones
    sentences = sent_tokenize(text)
    
    # Lista para almacenar las oraciones procesadas
    processed_sentences = []

    # Iterar sobre cada oración
    for sentence in sentences:
        # Procesar la oración con spaCy
        doc = nlp(sentence)
        
        # Filtrar las stop words
        filtered_words = [token.text for token in doc if not token.is_stop]
        
        # Unir las palabras filtradas en una oración
        processed_sentence = ' '.join(filtered_words)
        
        # Agregar la oración procesada a la lista
        processed_sentences.append(processed_sentence)

    return processed_sentences

def get_word_context(text, target_word, context_words_behine=2, context_words_after=5):
    """ Obtiene el contexto de una palabra objetivo en el texto. """
    words = word_tokenize(text)
    target_indices = [i for i, word in enumerate(words) if word.lower() == target_word.lower()]
    contexts = []

    for index in target_indices:
        start_index = max(0, index - context_words_behine)
        end_index = min(len(words), index + context_words_after + 1)  # +1 para incluir la palabra objetivo
        context = words[start_index:end_index]
        contexts.append(' '.join(context))

    return ' | '.join(contexts)

def encontrar_elemento_en_cadena(lista, cadena):
    """ Encuentra un elemento en la lista que se asemeje a la cadena dada. """
    return next((elemento for elemento in lista if fuzz.partial_ratio(elemento.lower(), cadena.lower()) >= UMBRAL_SIMILITUD), None)

def fist_analysis(lista_frases):
    for frase in lista_frases:
        for campo in User.CAMPOS:
            if fuzz.partial_ratio(campo.lower(), frase.lower()) >= UMBRAL_SIMILITUD:
                if campo in ['nodulo', 'microcalcificaciones', 'asimetrias']:
                    oracion = get_word_context(frase, campo)
                    result = analysis_of_feelings.analyze_feelings(oracion, OBJECT_ANALYSIS)
                    valor = User.CAMPOS[campo]['choices'][1] if len(User.CAMPOS[campo]['choices']) > 1 and result[0]['label'] >= "3 star" else User.CAMPOS[campo]['choices'][0]
                    if User.get_campo(campo) is None:
                        User.set_campo(campo, valor)
                else:
                    maximo = min(len(campo), 7)
                    found_choices = second_analysis(frase, campo[0:maximo], User.CAMPOS[campo]['choices'])
                    if found_choices and User.get_campo(campo) is None:
                        User.set_campo(campo, found_choices[0]) 
                    else:
                        # ## Función lógica para sacar más información
                        pass
            else:
                maximo = min(len(campo), 7)
                found_choices = second_analysis(frase, campo[0:maximo], User.CAMPOS[campo]['choices'])
                if found_choices and User.get_campo(campo) is None:
                    User.set_campo(campo, found_choices[0]) 
                else:
                    # ## Función lógica para sacar más información
                    pass

def second_analysis(text, search_term, choices):
    """ Análisis secundario para encontrar coincidencias con opciones dadas. """
    found_choices = []  # Inicializar la lista de opciones encontradas

    # Expresión regular para encontrar el término de búsqueda en el texto
    pattern = rf'(?i)({search_term}.*?)\.(?=\s|$)'  # Captura hasta el final de la oración

    # Buscar el término en el texto
    match = re.search(pattern, text)

    if match:
        # Obtener el texto que contiene el término de búsqueda
        hallazgo = match.group(0)

        # Comprobar si alguna de las opciones se menciona utilizando FuzzyWuzzy
        for choice in choices:
            similarity = fuzz.partial_ratio(hallazgo.lower(), choice.lower())
            if similarity > 70:  # Umbral de similitud (puedes ajustarlo)
                found_choices.append(choice)

    return found_choices  # Retornar las opciones encontradas

def correct_text(text):
    """ Corrige el texto eliminando acentos y caracteres especiales. """
    # Normalizar el texto a forma NFD y quitar los caracteres diacríticos
    normalized_text = unicodedata.normalize('NFD', text)
    text_without_accents = ''.join(c for c in normalized_text if unicodedata.category(c) != 'Mn')
    
    return text_without_accents

def filter_words(words, target_word, threshold):
    """ Filtra palabras similares a la palabra objetivo. """
    return [word for word in words if fuzz.partial_ratio(word.lower(), target_word.lower()) >= threshold]

def filter_phrases(phrases, target_word):
    """ Filtra frases que contienen la palabra objetivo. """
    return [phrase for phrase in phrases if fuzz.partial_ratio(target_word, phrase) >= UMBRAL_SIMILITUD]
