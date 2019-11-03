from data_access.html_data_dao import extrat_page_html, get_pagination_num
from preprocessing.metadata_reader import read_metadata
from data_access.html_data_dao import extrat_page_html, get_pagination_num
from preprocessing.details_reader import add_details
import pandas as pd
from datetime import datetime
from configuration.init_config import LOGGER
from commons.prov_dict import PROV_DICT


def build_df(eq_area):
    """
        Builds the final df: makes the calls to first gathers the metadata and then the details.
    """
    df_final = pd.DataFrame()
    get_num_pages = get_pagination_num(eq_area)
    if not get_num_pages:
        return None
    for i in range(1, int(get_num_pages)):
        LOGGER.info('\t {0:.2%}'.format(i/int(get_num_pages)) + '' + ' for {} completed.'.format(
            eq_area))
        data = extrat_page_html(eq_area, i)
        df = read_metadata(eq_area, data)
        asd = add_details(df)
        df_final = df_final.append(asd)
    LOGGER.info('\t 100%' + ' for {} completed.'.format(
        eq_area))
    return df_final


def get_area(str_area):
    if str_area == '*':
        LOGGER.info('Running code for ALL provinces')
        return list(PROV_DICT.keys())
    else:
        try:
            eq_area = PROV_DICT[str_area]
        except Exception as e:
            LOGGER.error(
                'Error retrieving data for area-key {} - {}'.format(str_area, e))
        finally:
            return eq_area


def is_areas_list(str_areas):
    if isinstance(str_areas, list):
        return True
    else:
        return False
