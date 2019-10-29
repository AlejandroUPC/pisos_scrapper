import click
from commons.prov_dict import PROV_DICT
from configuration.init_config import APP_CONFIG, LOGGER
from services.parsing_execution import build_df
import pandas as pd
from datetime import datetime


@click.group()
def run():
    pass


@run.command()
@click.argument('area', required=True)
def start_execution(area):
    now = datetime.now().strftime('%d-%m-%Y')
    if area == '*':
        df_global = pd.DataFrame()
        LOGGER.warning('Running code for ALL provinces')
        for key in PROV_DICT.keys():
            eq_area = PROV_DICT[key]
            LOGGER.warning(
                'Starting execution for area {}-{}'.format(area, eq_area))
            df_temp = build_df(eq_area)
            if df_temp is not None:
                df_global = df_global.append(df_temp, ignore_index=True)
        df_global.to_csv('{}Global_{}.csv'.format(APP_CONFIG['results_folder'],
                                                  now), encoding='cp1252')
    else:
        try:
            eq_area = PROV_DICT[area]
        except Exception as e:
            LOGGER.error(
                'Error trying to get data for abreviation {} - {}'.format(area, e))
        finally:
            LOGGER.warning(
                'Starting execution for area {}-{}'.format(area, eq_area))
            df_region = build_df(eq_area)
            df_region.to_csv('{}data_{}_{}.csv'.format(APP_CONFIG['results_folder'], eq_area, now),
                             encoding='cp1252')


if __name__ == '__main__':
    run()
