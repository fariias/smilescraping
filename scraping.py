from bs4 import BeautifulSoup
import requests


def request_from_url(url: str, params: dict = {}) -> dict():
    req = requests.get(url, params=params)
    content = {}

    if req.status_code == 200:
        print('Success!')
        content = req.content

    return content


def process_data(content: str) -> BeautifulSoup:
    soup = BeautifulSoup(content, 'html.parser')

    return soup


def search_flights():
    url = 'https://www.smiles.com.br/home'

    params = {
        'adults': 1,
        'children': 0,
        'infants': 0,
        'searchType': 'g3',
        'tripType': 1,
        'originAirport': 'RIO',
        'destinationAirport': 'NAT',
        'departureDate': 1571403600000,
        'returnDate': 1572008400000

    }

    request = request_from_url(url)
    processed_data = process_data(request)





if __name__ == '__main__':
    search_flights()