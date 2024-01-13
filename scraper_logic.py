import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        return [para.get_text().strip() for para in paragraphs if para.get_text().strip()]
    except requests.RequestException as e:
        print(f"Error during requests to {url}: {e}")
        return []