import click
from preprocessing.metadata_reader import read_metadata
from data_access.html_data_dao import extrat_page_html, get_pagination_num
from preprocessing.details_reader import add_details
import pandas as pd


@click.group()
def run():
    pass


@run.command()
# @click.argument('communities', required=True)
def start_execution():
    df_final = pd.DataFrame()
    get_num_pages = get_pagination_num()
    for i in range(1, int(get_num_pages)):
        print('Iteration {}'.format(i))
        data = extrat_page_html(i)
        df = read_metadata(data)
        asd = add_details(df)
        df_final = df_final.append(asd)
    df_final.to_csv('a.csv')


if __name__ == '__main__':
    run()
