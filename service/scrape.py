import globals
import requests
from bs4 import BeautifulSoup


def start_scrape(stock_name: str):
    """
    This service invokes the URL and fetches the current stock price for the requested stock name
    :param stock_name: str
    :return: None
    """
    local_url = globals.url.format(stock_name)
    response = requests.get(url=local_url, headers=globals.headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        container_class = soup.find('div', attrs={'class': 'aviV4d'})
        if container_class is not None:
            value = container_class.find('span', attrs={'class': 'IsqQVc NprOob wT3VGc'}).getText()
            unit = container_class.find('span', attrs={'class': 'knFDje'}).getText()
            print(f'{stock_name} value is {value} {unit}')
