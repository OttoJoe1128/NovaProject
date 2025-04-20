import requests
from bs4 import BeautifulSoup

class WebSpider:
    def __init__(self, url):
        self.url = url
    
    def fetch_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # HTTP istek hatalarını kontrol et
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Web tarayıcısı hatası: {e}")
            return None
    
    def parse_html(self, html_data):
        soup = BeautifulSoup(html_data, 'html.parser')
        headlines = soup.find_all('h1')  # Başlıkları bul
        return [headline.get_text() for headline in headlines]

    def get_headlines(self):
        html_data = self.fetch_data()
        if html_data:
            return self.parse_html(html_data)
        return []

