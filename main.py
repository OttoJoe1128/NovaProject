# main.py
from ecosystem_analyzer import EcosystemAnalyzer
from ecosystem_visualization import EcosystemVisualization
from sentiment_analysis import SentimentAnalysis
from web_spider import WebSpider

def fetch_and_analyze_headlines():
    # Web'den başlıkları al
    spider = WebSpider("https://www.bbc.com")
    headlines = spider.get_headlines()
    sentiments = []

    # Başlıkları analiz et
    if headlines:
        print("Güncel Başlıklar ve Duygu Analizi:")
        for index, headline in enumerate(headlines, 1):
            sentiment = SentimentAnalysis.analyze(headline)
            sentiments.append(sentiment)
            print(f"{index}. {headline} - Duygu Durumu: {sentiment}")

        # Duygu durumu görselleştirmesini yap
        DataVisualization.plot_sentiment_analysis(sentiments)
    else:
        print("Başlıklar alınamadı.")

# Çevresel verileri al
environmental_data = {"weather": [25, 22, 20], "soil_temp": [15, 16, 14], "biodiversity": [90, 85, 88]}
user_data = {"water_consumption": 100, "land_usage": 50}

# Ekosistem analizi yap
ecosystem_analyzer = EcosystemAnalyzer(environmental_data, user_data)
ecosystem_analyzer.generate_report()

# Ekosistem verilerini görselleştir
EcosystemVisualization.plot_environmental_data(environmental_data)

# Web başlıklarını al ve analiz et
fetch_and_analyze_headlines()
