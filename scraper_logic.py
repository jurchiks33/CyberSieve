import requests
from bs4 import BeautifulSoup

def scrape_website(url, tag=None, keyword=None, css_selector=None):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        if css_selector:
            elements = soup.select(css_selector)
        elif tag:
            elements = soup.find_all(tag)
            if keyword:
                elements = [el for el in elements if keyword.lower() in el.get_text().lower()]
        else:
            return [] 

        return [element.get_text().strip() for element in elements]

    except requests.RequestException as e:
        print(f"Error during requests to {url}: {e}")
        return []  