# ecosystem_analyzer.py

import requests

class EcosystemAnalyzer:
    def __init__(self, environmental_data, user_interaction_data):
        self.environmental_data = environmental_data
        self.user_interaction_data = user_interaction_data

    def analyze_environment(self):
        # Çevresel verilerle analiz yapar
        print("Çevresel durum analizi yapılıyor...")
        return {
            "hava_durumu": self.environmental_data["weather"],
            "toprak_sıcaklığı": self.environmental_data["soil_temp"],
            "biyoçeşitlilik": self.environmental_data["biodiversity"]
        }

    def analyze_user_impact(self):
        # Kullanıcı etkileşimleri ile çevresel etkiyi analiz eder
        print("Kullanıcı etkileşimlerinin çevresel etkisi analiz ediliyor...")
        return {
            "su_tüketimi": self.user_interaction_data["water_consumption"],
            "toprak_kullanımı": self.user_interaction_data["land_usage"]
        }

    def generate_report(self):
        environment_analysis = self.analyze_environment()
        user_impact = self.analyze_user_impact()
        
        print("Çevresel Rapor:")
        print(f"Hava Durumu: {environment_analysis['hava_durumu']}")
        print(f"Toprak Sıcaklığı: {environment_analysis['toprak_sıcaklığı']}")
        print(f"Biyoçeşitlilik: {environment_analysis['biyoçeşitlilik']}")
        
        print("Kullanıcı Etkisi Raporu:")
        print(f"Su Tüketimi: {user_impact['su_tüketimi']}")
        print(f"Toprak Kullanımı: {user_impact['toprak_kullanımı']}")
