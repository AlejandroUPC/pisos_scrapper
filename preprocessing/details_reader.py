import pandas as pd
from bs4 import BeautifulSoup
import requests
from data_access.html_data_dao import extract_details_page_html
from commons.details_dict import BASICDATA_DICT, INQDATA_DICT
from commons.utils import text_parsing
from configuration.init_config import LOGGER, APP_CONFIG
from preprocessing.download_images import download_images

CLASS_PREFIX = r'icon icon-inline icon-default icon-{}'


def add_details(df):
    """
        Adds the details from every flat based on the index.
    """
    list_ids = df.index
    for id_x in list_ids:
        details_html = extract_details_page_html(
            df.loc[id_x, 'Link'])
        row_to_append = __parse_data(details_html)
        for keys in row_to_append:
            df.loc[id_x, keys] = row_to_append[keys]
        if APP_CONFIG['donwload_flat_photos']:
            download_images(details_html)
    return df


def __parse_data(str_html):
    """
        Parses some of the data to find all the individual attributes.
    """
    details_block = str_html.findAll(
        'ul', {'class': 'charblock-list charblock-basics'}, limit=None)
    for item in details_block:
        dict_row = __parse_individual_attr(item)
    for keys in INQDATA_DICT.keys():
        get_next_span_text = str_html.find(
            'span', text=keys)
        if get_next_span_text:
            get_next_span_text = text_parsing.extract_text(
                get_next_span_text.findNext('span').text)
        dict_row[keys] = get_next_span_text
    return dict_row


def __parse_individual_attr(str_html_data):
    """
        Checks the key-value to find how to extract each attribute based on the config dict.
    """
    TEMP_DICT = BASICDATA_DICT.fromkeys(BASICDATA_DICT, 0)
    for key in BASICDATA_DICT.keys():
        str_list_item = str_html_data.find(
            'span', {'class': CLASS_PREFIX.format(key)})
        if str_list_item:
            if BASICDATA_DICT[key] == 'NNS':
                TEMP_DICT[key] = __extract_nns(str_list_item)
            elif BASICDATA_DICT[key] == 'TNS':
                TEMP_DICT[key] = __extract_tns(str_list_item)
            elif BASICDATA_DICT[key] == 'TSS':
                TEMP_DICT[key] = str_list_item.text
    return TEMP_DICT


def __parse_inq_data(str_html):
    details_block = str_html.findAll(
        'h2', text='Inquilinos', limit=None)
    details_block = details_block.findNext('div', {'class': 'charblock-right'})
    for item in details_block:
        dict_row = __parse_individual_inq_attr(item)
        return dict_row


def __parse_individual_inq_attr(str_html_data):
    """
        Checks the key-value to find how to extract each attribute based on the config dict.
    """
    TEMP_DICT = INQDATA_DICT.fromkeys(INQDATA_DICT, 0)
    for key in INQDATA_DICT.keys():
        str_list_item = str_html_data.find(
            'span', {'class': CLASS_PREFIX.format(key)})
        if str_list_item:
            TEMP_DICT[key] = __extract_tns(str_list_item)
    return TEMP_DICT


def __extract_nns(str_html_data):
    """
    Extracts the data for the nns type (no next span).
    """
    data_str = str_html_data.findNext('span')
    data_str = text_parsing.extract_numbers(data_str.text)
    return data_str


def __extract_tns(str_htlm_data):
    """
    Extracts the data for tns (text next span).
    """
    data_str = str_htlm_data.findNext('span').text
    if data_str:
        data_str = text_parsing.extract_text(data_str)
    return data_str
