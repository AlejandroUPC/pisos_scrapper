from bs4 import BeautifulSoup
import requests
from configuration.init_config import LOGGER, APP_CONFIG
import time


def get_pagination_num(eq_area):
    """
        Gets the number of paginations needed. If no iteration item is found 2 is returned, so in the range (1,2) will run the iteration just once.
    """
    __wait_request()
    page = requests.get(
        '{}alquiler/{}/'.format(APP_CONFIG['main_url'], eq_area))
    __check_request(page)
    soup = BeautifulSoup(page.content, features="html.parser")
    get_num_pages = soup.find(
        'div', {'class': 'pager'})
    try:
        get_num_pages = get_num_pages.findAll('a', {'class': 'item'})[-1].text
    except Exception:
        get_num_pages = 2
    return get_num_pages


def extrat_page_html(eq_area, pag_num):
    """
        Gets the entire html page with all the listed flats.
    """

    page = requests.get(
        '{}/alquiler/{}/{}/'.format(APP_CONFIG['main_url'], eq_area, pag_num))
    __check_request(page)
    soup = BeautifulSoup(page.content, features="html.parser")
    return soup


def extract_details_page_html(str_link):
    """
        Gets the specific html page with the details for every flat.
    """
    __wait_request()
    page = requests.get(
        '{}{}'.format(APP_CONFIG['main_url'], str_link.strip()))
    __check_request(page)
    soup = BeautifulSoup(page.content, features="html.parser")
    return soup


def __check_request(item_page):
    if item_page.status_code != 200:
        LOGGER.error('An error ocurred while handling the request')
        return None


def __wait_request():
    if APP_CONFIG['wait_requests']:
        time.sleep(APP_CONFIG['second_between_reqs'])
        LOGGER.info('Waiting {} between requests'.format(
            APP_CONFIG['second_between_reqs']))
