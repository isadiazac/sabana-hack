from transformers import pipeline

class AnalysisOfFeelings:
    def __init__(self):
        self.sentiment_analysis = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def prepare():
    # Cargar el pipeline de análisis de sentimientos
    return  AnalysisOfFeelings()

def analyze_feelings(text, AnalysisOfFeelings):
    # Analizar el sentimiento del texto
    return AnalysisOfFeelings.sentiment_analysis(text)