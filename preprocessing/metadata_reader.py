from bs4 import BeautifulSoup
import requests
from data_access.html_data_dao import extrat_page_html
import pandas as pd
import re
from commons.utils import text_parsing
COLS_DATA = ['Id', 'Location', 'Price', 'Descr', 'Link', 'superficieutil',
             'habitacionamueblada', 'numbanos', 'estadoconservacion', 'gastosincluidosalquiler']


def read_metadata(html_flat_list):
    list_flats = __extract_flat_divs(html_flat_list)
    df_data = pd.DataFrame(
        columns=COLS_DATA)
    for item in list_flats:
        unique_id = item.find(
            'div', {'class': 'item favorito hide showExcept600'})['data-internal-fv']
        locatin = __clear_text_from_tag(
            item.find('div', {'class': 'location'}))
        price = __clear_text_from_tag(item.find('div', {'class': 'price'}))
        price = text_parsing.extract_numbers(price)
        descr = __clear_text_from_tag(
            item.find('div', {'class': 'description'}))
        extra_link = item.find('a', {'class': 'anuncioLink'})['href']
        df_data = df_data.append(__parse_df_row('{};{};{};{};{}'.format(
            unique_id.strip(), locatin, price, descr, extra_link.strip())), ignore_index=True)
    df_data.set_index(keys='Id', inplace=True)
    return df_data


def __extract_flat_divs(html_text):
    all_flats = html_text.findAll('div', {'class': 'row clearfix'}, limit=None)
    return all_flats


def __clear_text_from_tag(str_item):
    if str_item:
        return str_item.text.strip().replace("\n", "")
    else:
        return str_item


def __parse_df_row(str_row_item):
    Id, Location, Price, Descr, Link = str_row_item.split(';')
    str_append = {'Id': Id, 'Location': Location,
                  'Price': Price, 'Descr': Descr, 'Link': Link}
    return str_append


def __get_id_by_regex(str_data):
    """
    For some reason i ccant find first
    """
