from bs4 import BeautifulSoup
from selenium import webdriver
from furl import furl
import chromedriver_binary
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def request_from_url(url: str, params: dict = {}) -> dict():

    f_url = furl(url)
    f_url.args = params

    options = webdriver.ChromeOptions()
    options.add_argument("javascript.enabled")
    options.add_argument("--enable-javascript")

    browser = webdriver.Chrome('chromedriver', options=options)
    browser.get(f_url.url)

    element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, '//*[@id="alertModalLoading"]')))

    html = browser.page_source

    return html


def process_data_with_soap(content: str) -> BeautifulSoup:
    soup = BeautifulSoup(content, 'lxml')

    return soup


def search_flights():
    url = 'https://www.smiles.com.br/emissao-com-milhas'

    params = {
        'adults': 1,
        'children': 0,
        'infants': 0,
        'searchType': 'g3',
        'tripType': 1,
        'originAirport': 'RIO',
        'destinationAirport': 'NAT',
        'departureDate': 1576760400000,
        'returnDate': 1578056400000
    }

    request = request_from_url(url, params)
    soup = process_data_with_soap(request)

    first_flights = soup.find_all(id='firstFlights')
    for flight in first_flights:
        print(flight)



if __name__ == '__main__':
    search_flights()