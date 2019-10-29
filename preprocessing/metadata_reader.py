from bs4 import BeautifulSoup
import requests
from data_access.html_data_dao import extrat_page_html
import pandas as pd
import re
from commons.utils import text_parsing
COLS_DATA = ['Id', 'Location', 'Price', 'Descr', 'Link', 'superficieutil',
             'habitacionamueblada', 'numhabitaciones', 'numbanos', 'estadoconservacion', 'gastosincluidosenalquiler ', 'Número de inquilinos', 'Edad mínima', 'Género']


def read_metadata(eq_area, html_flat_list):
    """
        Reads the metadata (Id,location,price,descr and extra_link) from every flat.
    """
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
        df_data = df_data.append(__parse_df_row('{}^{}^{}^{}^{}'.format(
            unique_id.strip(), locatin, price, descr, extra_link.strip())), ignore_index=True)
    df_data.set_index(keys='Id', inplace=True)
    df_data['area'] = eq_area.replace('habitaciones-', '')
    return df_data


def __extract_flat_divs(html_text):
    """
        Extracts all the divs that contain the details from the flat.
    """
    all_flats = html_text.findAll('div', {'class': 'row clearfix'}, limit=None)
    return all_flats


def __clear_text_from_tag(str_item):
    """
        Clears some of the characters found in the data.
    """
    if str_item:
        return str_item.text.strip().replace("\n", "").replace(':', '')
    else:
        return str_item


def __parse_df_row(str_row_item):
    """
        Parses the string separating it by a defined char to be directly appended to the dataframe.
    """
    Id, Location, Price, Descr, Link = str_row_item.split('^')
    str_append = {'Id': Id, 'Location': Location,
                  'Price': Price, 'Descr': Descr, 'Link': Link}
    return str_append
