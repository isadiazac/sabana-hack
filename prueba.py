from transformers import pipeline

def train():

    sentiment_pipeline = pipeline("sentiment-analysis")
    result = sentiment_pipeline("El servicio fue increíble, estoy muy satisfecho")
    print("Sentimiento:", result)
