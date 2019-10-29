from bs4 import BeautifulSoup
import requests


def get_pagination_num():
    page = requests.get(
        'https://www.pisos.com/alquiler/habitaciones-barcelona/')
    soup = BeautifulSoup(page.content)
    get_num_pages = soup.find(
        'a', {'data-click-analytics': 'clic-parrilla,paginador,pagina-23-v2'}).text
    return get_num_pages


def extrat_page_html(pag_num):
    print('Checking url {}'.format(
        'https://www.pisos.com/alquiler/habitaciones-barcelona/{}/'.format(pag_num)))
    page = requests.get(
        'https://www.pisos.com/alquiler/habitaciones-barcelona/{}/'.format(pag_num))
    soup = BeautifulSoup(page.content)
    return soup


def extract_details_page_html(str_link):
    page = requests.get(
        'https://www.pisos.com{}'.format(str_link.strip()))
    soup = BeautifulSoup(page.content)
    return soup
