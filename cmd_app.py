import click
from commons.prov_dict import PROV_DICT
from configuration.init_config import APP_CONFIG, LOGGER
from services.parsing_execution import build_df
from services import graphicating_data
import pandas as pd
from datetime import datetime


@click.group()
def run():
    pass


@run.command()
@click.argument('area', required=True)
def start_execution(area):
    start = datetime.now()
    now = start.strftime('%d-%m-%Y')
    if area == '*':
        df_global = pd.DataFrame()
        LOGGER.info('Running code for ALL provinces')
        for key in PROV_DICT.keys():
            eq_area = PROV_DICT[key]
            LOGGER.info(
                'Starting execution for area: {}'.format(eq_area))
            df_temp = build_df(eq_area)
            if df_temp is not None:
                df_global = df_global.append(df_temp, ignore_index=True)
        df_global.to_csv('{}Global_{}.csv'.format(APP_CONFIG['results_folder'],
                                                  now), encoding='cp1252', sep='|')
    else:
        try:
            eq_area = PROV_DICT[area]
        except Exception as e:
            LOGGER.error(
                'Error trying to get data for abreviation {} - {}'.format(area, e))
        finally:
            LOGGER.info(
                'Starting execution for area {}-{}'.format(area, eq_area))
            df_region = build_df(eq_area)
            df_region.to_csv('{}data_{}_{}.csv'.format(APP_CONFIG['results_folder'], eq_area, now),
                             encoding='cp1252', sep='|')

    if APP_CONFIG['plot_data']:
        graphicating_data.create_graph()
    LOGGER.info('Completed the process in {} seconds'.format(
        datetime.now()-start))


if __name__ == '__main__':
    run()
