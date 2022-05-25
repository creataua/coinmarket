import requests
from bs4 import BeautifulSoup
from main import get_monet, get_url, url

html= get_url(url)
monet = get_monet(html)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

for item in monet:
    dc_attr = {'class': 'cmc-link', 'href': f'/currencies/{item}/'}
    try:
        name = soup.find('a', dc_attr).find('p').text
        price = soup.find('a', dc_attr).parent.find_next_sibling()
        print(f"{name} - {price.text}")
    except AttributeError:
        print(f"Монета {item.title()} пропала с трендов Coinmarket")
        continue

