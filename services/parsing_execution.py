from data_access.html_data_dao import extrat_page_html, get_pagination_num
from preprocessing.metadata_reader import read_metadata
from data_access.html_data_dao import extrat_page_html, get_pagination_num
from preprocessing.details_reader import add_details
import pandas as pd
from datetime import datetime


def build_df(eq_area):
    df_final = pd.DataFrame()
    get_num_pages = get_pagination_num(eq_area)
    if not get_num_pages:
        return None
    for i in range(1, int(get_num_pages)):
        print('Iteration {}'.format(i))
        data = extrat_page_html(eq_area, i)
        df = read_metadata(eq_area, data)
        asd = add_details(df)
        df_final = df_final.append(asd)
    return df_final
