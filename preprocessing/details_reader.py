import pandas as pd
from bs4 import BeautifulSoup
import requests
from data_access.html_data_dao import extract_details_page_html
from commons.details_dict import DETAILS_DICT
from commons.utils import text_parsing

CLSAS_PREFIX = r'icon icon-inline icon-default icon-{}'


def add_details(df):
    list_ids = df.index
    for id_x in list_ids:
        details_html = extract_details_page_html(
            df.loc[id_x, 'Link'])
        print('Checking url {}'.format(
            df.loc[id_x, 'Link']))
        row_to_append = __parse_data(details_html)
        for keys in row_to_append:
            df.loc[id_x, keys] = row_to_append[keys]
    return df


def __parse_data(str_html):
    details_block = str_html.findAll(
        'ul', {'class': 'charblock-list charblock-basics'}, limit=None)
    for item in details_block:
        dict_row = __parse_individual_attr(item)
        return dict_row


def __parse_individual_attr(str_html_data):
    """
    Todo check if its none
    """
    TEMP_DICT = DETAILS_DICT.fromkeys(DETAILS_DICT, 0)
    for key in DETAILS_DICT.keys():
        str_list_item = str_html_data.find(
            'span', {'class': CLSAS_PREFIX.format(key)})
        if str_list_item:
            if DETAILS_DICT[key] == 'NNS':
                TEMP_DICT[key] = __extract_nns(str_list_item)
            elif DETAILS_DICT[key] == 'TNS':
                TEMP_DICT[key] = __extract_tns(str_list_item)
            elif DETAILS_DICT[key] == 'TSS':
                TEMP_DICT[key] = str_list_item.text
    return TEMP_DICT


def __extract_nns(str_html_data):
    data_str = str_html_data.findNext('span')
    data_str = text_parsing.extract_numbers(data_str.text)
    return data_str


def __extract_tns(str_htlm_data):
    data_str = str_htlm_data.findNext('span').text
    return data_str
