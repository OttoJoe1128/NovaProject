# ecosystem_visualization.py
import matplotlib.pyplot as plt

class EcosystemVisualization:
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
