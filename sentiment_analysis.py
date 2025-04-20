# sentiment_analysis.py

from textblob import TextBlob

class SentimentAnalysis:
    @staticmethod
    def analyze(text):
        analysis = TextBlob(text)
        # Pozitif, Negatif ve Nötr duygu durumları
        if analysis.sentiment.polarity > 0:
            return "Olumlu"
        elif analysis.sentiment.polarity < 0:
            return "Olumsuz"
        else:
            return "Nötr"
