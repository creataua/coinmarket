import requests
from bs4 import BeautifulSoup



url = "https://coinmarketcap.com/trending-cryptocurrencies"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
}

def get_url(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return "Error"


def get_monet(html):
    soup = BeautifulSoup(html, "lxml")
    data = soup.find_all("a", class_="cmc-link")
    monet = []
    for item in data:
        href = item.get('href')
        try:
            if '/currencies/' in href:
                monet.append(href.replace("/currencies/", "").replace("/", ""))
        except TypeError:
            pass
    result_list = list(set(monet))
    return result_list
  

def main():
    html = get_url(url)
    monet = get_monet(html)
    #print(monet)
    



if __name__ == "__main__":
    main()
