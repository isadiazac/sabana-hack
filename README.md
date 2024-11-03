# Ficha Técnica - VitalTrack

## Descripción breve

VitalTrack es un algoritmo que lee, analiza y clasifica las bases de datos clínicos para facilitar la digitación de las historias a las bases y evitar errores tipográficos, de entrada manual, codificación y de formato incorrectos.

## Nivel de desarrollo

El nivel de desarrollo se encuentra en una fase intermedia (Prototipo Funcional). Las funcionalidades básicas están implementadas y operativas, pero se requiere más trabajo en aspectos como la optimización del rendimiento, la mejora de la precisión en el análisis emocional y la creación de una interfaz amigable para el usuario

## Link al video

[Video de presentación](URL)

## Ventajas o fortalezas de nuestra propuesta

_1. Procesamiento de Lenguaje Natural Avanzado_
1.1. Utiliza bibliotecas como NLTK y spaCy para un análisis lingüístico sofisticado.
1.2. Implementa técnicas avanzadas como tokenización, extracción de entidades y generación de n-gramas.

_2. Flexibilidad en el Análisis_
2.1. Puede analizar diferentes campos médicos (nódulos, calcificaciones, asimetrías, etc.) de manera adaptable para otras investigaciones futuras.
2.2. Permite la configuración de umbrales de similitud para ajustar la sensibilidad del análisis.

_3. Análisis Contextual:_
3.1. Examina las palabras en su contexto (Historia clínica o Estudio), mejorando la precisión de la interpretación.
3.2. Utiliza técnicas de coincidencia difusa (Funza matching) para identificar palabras y frases relevantes.

_4. Estructura Modular:_
4.1. El código está organizado en funciones separadas, facilitando el mantenimiento y la expansión futura.

_5. Análisis de Sentimientos_
5.1. Se incorporo el análisis de sentimiento para campos específicos como nódulos, microcalcificaciones y asimetrías.

_6. Personalización_
6.1 Permite la configuración de campos de análisis a través de la clase "Usher", ofreciendo flexibilidad para diferentes tipos de informes médicos.

## Desventajas o debilidades de nuestra propuesta

_1. Expansión de la extracción de datos_
1.1. Posibilidad de ampliar el alcance para capturar una gama más completa de variables clínicas, mejorando la comprensión de cada caso específico.

_2. Optimización de dependencias_
2.1. Potencial para consolidar funcionalidades para mejorar la eficiencia y facilitar el mantenimiento a largo plazo del sistema.

_3. Simplificación y modularización_
3.1. Oportunidad para refinar aún más la estructura del código, haciéndolo más accesible y fácil de mantener sin sacrificar funcionalidad, facilitando futuras expansiones y adaptaciones.

## Detalles técnicos

- _Tecnologías utilizadas_:
  _1. Python:_ Lenguaje de programación principal para el desarrollo del prototipo.
  _2. spaCy:_ Biblioteca de procesamiento de lenguage natural (NLP) utilizada para la tokenización, análisis de entidades y generación de n-gramas, facilitando el entendimiento del texto en español.
  _3. NLTK:_ Conocido como Natural Lenguage ToolKit, fue utilizado para la tokenización y manipulación de texto, espcialmente para trabajar con n-gramas y análisis linguístico.
  _4. FuzzyWuzzy:_ Biblioteca para comparacion de cadenas que permite filtrar palabras y frases similares mediante algoritmos de coincidencia difusa.
  _5. Transformer:_ Es fundamental para el desarrollo, ya que permite acceder a modelos avanzados de PNL y facilitar su uso a traves de la interfaz de "Pipeline".

- _Herramientas usadas_:
  _1. Word_tokenize:_ Utilizada para la tokenización de texto, permitiendo dividir el texto en palabras individuales.
  _2. Fuzz:_ utilizada para la comparación de cadenas, que permite medir la similitud entre palabras y frases mediante algoritmos de coincidencia difusa.
  _3. analysis_of_feelings:_ Importa un módulo que se encarga del análisis de sentimientos, sugiriendo que contiene funciones específicas para evaluar las emociones en el texto.

- _Alcance del prototipo_: El prototipo está diseñado para analizar datos textuales de pacientes, extrayendo sentimientos y palabras clave relevantes mediante técnicas de procesamiento de lenguaje natural. Utiliza tokenización y n-gramas para identificar entidades significativas y evaluar el tono emocional de las entradas. Al filtrar información relevante y contextualizar términos clave, el sistema proporciona herramientas valiosas para que los profesionales de la salud mejoren la calidad del cuidado.
  _Limitaciones_
  _Dependencia del umbral de similitud:_ Un umbral fijo para determinar la similitud de palabras puede no ser adecuado en todos los contextos, lo que podría resultar en la omisión de información crítica o en la inclusión de datos irrelevantes.

## Repositorio del proyecto

[Repositorio del equipo](URL)
