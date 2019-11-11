
from bs4 import BeautifulSoup
import requests
import re


def download_images(str_html_data):
    img_href = __get_image_path(str_html_data)
    pass


def __get_image_path(str_html_data):
    image_path = str_html_data.find(
        'div', {'id': 'mainPhotoImage'})['style']
    clean_link = __parse_url_form_html(image_path)
    return clean_link


def __parse_url_form_html(str_html_tag):
    regex_pattern = r'(?<=\(")(.*)(?=\"))'
    path_jpg = re.match(regex_pattern, str_html_tag)
    if path_jpg:
        return path_jpg
    else:
        return None
