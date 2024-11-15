import requests
from bs4 import BeautifulSoup

VALOR_MAXIMO = 30.00
VALOR_MINIMO = 10.00

def fetchPage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        return response.text
    
    except requests.RequestException as e:
        print(f"Erro ao buscar a página: {e}")
        return None

def getDiscountProducts(pageContent):
    soup = BeautifulSoup(pageContent, 'html.parser')
    products = []
    
    for product in soup.select('ol li'):
        title = product.select_one('h3 a').get('title').strip()
        price = product.select_one('.price_color').text.replace('£', '').replace('Â', '').strip()
        url = product.select_one('h3 a').get('href').strip()
        
        url = 'https://books.toscrape.com/' + url
        if(float(price) < VALOR_MAXIMO and float(price) > VALOR_MINIMO):
            products.append({
                'title': title,
                'price': price,
                'url': url
            })
    return products