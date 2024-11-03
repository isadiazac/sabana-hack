import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import spacy
import pandas as pd

# Descargar stopwords y modelo de spaCy si es necesario
nltk.download("stopwords")
stop_words = set(stopwords.words("spanish"))  # Cambia a tu idioma si es otro

# Cargar el modelo de idioma en spaCy
nlp = spacy.load("es_core_news_sm")  # Cambia a "en_core_web_sm" si es en inglés

# Lista de historias clínicas
historias = [
    " Indicaciones: Mastalgia derecha. no se cuenta con estudios previos.   Técnica: Se realiza mamografía digital bilateral con compresión graduada en proyecciones CC y MLO con tomosíntesis e imagen sintética 2D.   Dosis media glandular:  5. 56 mGy.   Hallazgos: Las mamas son simétricas. Hay presencia de parénquima mamario bilateral retroareolar central de morfología dendrítica y de predominio derecho No hay nódulos, zonas de distorsión ni microcalcificaciones que sugieran malignidad. La piel y los complejos areola - pezón son normales. Las regiones axilares tienen ganglios con centro hipodenso.   Conclusión: Hallazgos están en relación a ginecomastia bilateral de patrón dendritico de predominio derecho Hallazgos benignos BIRADS 2.   Se sugiere continuar con control mamográfico anual.MEDICO RADIOLOGO: Edgar Ivan Gonzalez Rodriguez   RM: 797-2007       2019-01-14 07:22:15",
    " Indicaciones: Paciente con antecedente de ca próstata 2004, diagnostico de carcinoma ductal de mama izquierda, mastectomía izquierda, seroma. Control.    Técnica: Se realiza mamografía digital unilateral derecha con compresión graduada en proyecciones CC y MLO con tomosíntesis e imagen sintética 2D.   Dosis media glandular: 2.59 mGy.   Hallazgos: Hay presencia de parénquima mamario de morfología difusa. No hay nódulos, zonas de distorsión ni microcalcificaciones que sugieran malignidad. La piel y el complejo areola - pezón son normales. La región axilar tiene ganglios con centro hipodenso.   Conclusión: Hallazgos que están en relación a ginecomastia de patrón difuso. BIRADS 2.MEDICO RADIOLOGO: Edgar Ivan Gonzalez Rodriguez   RM: 797-2007       3/01/2022 12:14:38 p. m.",
    " Indicaciones: Paciente con antecedente de ca próstata 2004, diagnostico de carcinoma ductal de mama izquierda, mastectomía izquierda. Cuento con estudio mamográfico previo de enero de 2022.   Técnica: Se realiza mamografía digital unilateral derecha con compresión graduada en proyecciones CC y MLO obteniendo imágenes en tomosíntesis y sintétizada.    Hallazgos: Hay presencia de parénquima mamario de patrón difuso. No hay nódulos, zonas de distorsión ni microcalcificaciones que sugieran malignidad. La piel y el complejo areola - pezón son normales. La región axilar tiene ganglios con centro hipodenso. No hay cambios evolutivos significativos al comparar con estudios previos.   Conclusión: Hallazgos que están en relación a ginecomastia de patrón difuso. No se observan lesiones sospechosas. Hallazgos benignos BIRADS 2.MEDICO RADIOLOGO: Edgar Ivan Gonzalez Rodriguez   RM: 797-2007       19/12/2022 1:31:14 p. m.",
    " Indicaciones: Control anual por antecedente de neoplasia en mama izquierda  tratada con mastectomía. Se cuenta con estudios previos de 2022. Antecedente de carcinoma de próstata.   Técnica: Se realiza mamografía digital unilateral derecha con compresión graduada en proyecciones CC y MLO obteniendo imágenes en tomosíntesis y sintétizada.     Hallazgos: Hay presencia de parénquima mamario con un patrón difuso. No hay nódulos, zonas de distorsión ni microcalcificaciones que sugieran malignidad. La piel y el complejo areola - pezón son normales. La región axilar tiene ganglios con centro hipodenso. No hay cambios evolutivos significativos al comparar con estudios previos.   Conclusión: Hallazgos están en relación a ginecomastia de patrón difuso. Hallazgos benignos BIRADS 2.MEDICO RADIOLOGO:Edgar Ivan Gonzalez Rodriguez RM: 797-2007 30/09/2023 11:54:25 a. m.",
    " Indicaciones: Antecedente de cuadrantectomía izquierda en 2004 extra INC. Cuadrantectomía central derecha en julio 2016 por Ca in situ (segundo primario). No se cuenta con estudios previos.  Técnica: Se realiza mamografía digital bilateral con compresión graduada en proyecciones CC y MLO con tomosíntesis e imagen sintética 2D.   Dosis media glandular:  7. 35 mGy.   Hallazgos: Las mamas son simétricas. El parénquima mamario es fibroglandular disperso. Zona de distorsión con engrosamiento y retracción de la piel en región centro mamaria bilateral asociado a calcificaciones distróficas y clips de reparo quirúrgico en el lado derecho. No hay nódulos, zonas de distorsión ni microcalcificaciones que sugieran malignidad. Los complejos areola - pezón son normales. La región axilar está libre.   Conclusión: Cambios posquirurgicos bilaterales sin signos de recaída loco-regional. Hallazgos benignos BIRADS 2.   Se sugiere continuar con control mamográfico anual.MEDICO RADIOLOGO: Edgar Ivan Gonzalez Rodriguez   RM: 797-2007       2019-06-17 13:13:01"
]

# Función para limpiar el texto, eliminando palabras comunes y puntuación
def limpiar_texto(texto):
    doc = nlp(texto.lower())  # Convertir a minúsculas
    palabras_limpias = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(palabras_limpias)

# Limpiar cada historia
historias_limpias = [limpiar_texto(historia) for historia in historias]

# Vectorizar usando TF-IDF para identificar las palabras clave
vectorizer = TfidfVectorizer(max_df=0.8, min_df=2, max_features=1000)
tfidf_matrix = vectorizer.fit_transform(historias_limpias)

# Convertir a un DataFrame para ver la importancia de cada palabra
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())

# Función para obtener las palabras clave más importantes por historia
def palabras_clave_por_historia(row, num_palabras=5):
    palabras_ordenadas = row.sort_values(ascending=False)
    return palabras_ordenadas.index[:num_palabras].tolist()

# Obtener palabras clave para cada historia
palabras_clave_historias = tfidf_df.apply(palabras_clave_por_historia, axis=1)

# Mostrar cada historia con sus palabras clave
for idx, (historia, palabras_clave) in enumerate(zip(historias, palabras_clave_historias)):
    print(f"Historia {idx + 1}:")
    print("Texto:", historia)
    print("Palabras clave:", palabras_clave)
    print("-" * 40)
