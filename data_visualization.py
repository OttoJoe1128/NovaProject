# data_visualization.py

import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualization:
    @staticmethod
    def plot_sentiment_analysis(sentiments):
        sentiment_count = {"Olumlu": 0, "Olumsuz": 0, "Nötr": 0}
        
        for sentiment in sentiments:
            sentiment_count[sentiment] += 1

        # Grafik oluşturma
        sns.barplot(x=list(sentiment_count.keys()), y=list(sentiment_count.values()))
        plt.title('Duygu Durumu Analizi')
        plt.xlabel('Duygu Durumu')
        plt.ylabel('Başlık Sayısı')
        plt.show()
        
    @staticmethod
    def plot_environmental_data(environment_data):
        weather = environment_data.get("weather", [])
        biodiversity = environment_data.get("biodiversity", [])

        # Grafik oluşturma
        plt.figure(figsize=(10, 6))
        plt.plot(weather, label="Hava Durumu")
        plt.plot(biodiversity, label="Biyoçeşitlilik")
        plt.title("Çevresel Durum Analizi")
        plt.xlabel("Zaman")
        plt.ylabel("Değer")
        plt.legend()
        plt.show()
