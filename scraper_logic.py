import requests
from bs4 import BeautifulSoup

def scrape_website(url, tag, keyword=None):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        elements = soup.find_all(tag)

        if keyword:
            filtered_elements = [el for el in elements if keyword.lower() in el.get_text().lower()]
        else:
            filtered_elements = elements
        
        return [el.get_text().strip() for el in filtered_elements]

    except requests.RequestException as e:
        print(f"Error during requests to {url}: {e}")
        return []