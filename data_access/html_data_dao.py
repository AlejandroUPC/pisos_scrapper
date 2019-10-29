from bs4 import BeautifulSoup
import requests
from configuration.init_config import LOGGER, APP_CONFG
import time


def get_pagination_num(eq_area):
    if APP_CONFG['wait_requests']:
        time.sleep(APP_CONFG['second_between_reqs'])
        LOGGER.warning('Waiting {} between requests'.format(
            APP_CONFG['second_between_reqs']))
    page = requests.get(
        'https://www.pisos.com/alquiler/{}/'.format(eq_area))
    if page.status_code != 200:
        LOGGER.error('An error ocurred during handling request')
        return -1
    soup = BeautifulSoup(page.content)
    get_num_pages = soup.find(
        'div', {'class': 'pager'})
    try:
        get_num_pages = get_num_pages.findAll('a', {'class': 'item'})[-1].text
    except Exception:
        get_num_pages = None
    return get_num_pages


def extrat_page_html(eq_area, pag_num):
    if APP_CONFG['wait_requests']:
        time.sleep(APP_CONFG['second_between_reqs'])
        LOGGER.warning('Waiting {} between requests'.format(
            APP_CONFG['second_between_reqs']))
    page = requests.get(
        'https://www.pisos.com/alquiler/{}/{}/'.format(eq_area, pag_num))
    if page.status_code != 200:
        LOGGER.error('An error ocurred during handling request')
        return -1
    soup = BeautifulSoup(page.content)
    return soup


def extract_details_page_html(str_link):
    if APP_CONFG['wait_requests']:
        time.sleep(APP_CONFG['second_between_reqs'])
        LOGGER.warning('Waiting {} between requests'.format(
            APP_CONFG['second_between_reqs']))
    page = requests.get(
        'https://www.pisos.com{}'.format(str_link.strip()))
    if page.status_code != 200:
        LOGGER.error('An error ocurred during handling request')
        return -1
    soup = BeautifulSoup(page.content)
    return soup
