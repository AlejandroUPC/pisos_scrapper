from bs4 import BeautifulSoup
import requests
from configuration.init_config import LOGGER, APP_CONFIG
import time


def get_pagination_num(eq_area):
    if APP_CONFIG['wait_requests']:
        time.sleep(APP_CONFIG['second_between_reqs'])
        LOGGER.warning('Waiting {} between requests'.format(
            APP_CONFIG['second_between_reqs']))
    page = requests.get(
        '{}alquiler/{}/'.format(APP_CONFIG['main_url'], eq_area))
    if page.status_code != 200:
        LOGGER.error('An error ocurred during handling request')
        return -1
    soup = BeautifulSoup(page.content, features="html.parser")
    get_num_pages = soup.find(
        'div', {'class': 'pager'})
    try:
        get_num_pages = get_num_pages.findAll('a', {'class': 'item'})[-1].text
    except Exception:
        get_num_pages = None
    return get_num_pages


def extrat_page_html(eq_area, pag_num):
    if APP_CONFIG['wait_requests']:
        time.sleep(APP_CONFIG['second_between_reqs'])
        LOGGER.warning('Waiting {} between requests'.format(
            APP_CONFIG['second_between_reqs']))
    page = requests.get(
        '{}/alquiler/{}/{}/'.format(APP_CONFIG['main_url'], eq_area, pag_num))
    if page.status_code != 200:
        LOGGER.error('An error ocurred during handling request')
        return -1
    soup = BeautifulSoup(page.content, features="html.parser")
    return soup


def extract_details_page_html(str_link):
    if APP_CONFIG['wait_requests']:
        time.sleep(APP_CONFIG['second_between_reqs'])
        LOGGER.warning('Waiting {} between requests'.format(
            APP_CONFIG['second_between_reqs']))
    page = requests.get(
        '{}{}'.format(APP_CONFIG['main_url'], str_link.strip()))
    if page.status_code != 200:
        LOGGER.error('An error ocurred during handling request')
        return -1
    soup = BeautifulSoup(page.content, features="html.parser")
    return soup
