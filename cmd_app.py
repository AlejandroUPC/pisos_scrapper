import click
from commons.prov_dict import PROV_DICT
from configuration.init_config import APP_CONFIG, LOGGER
from services.parsing_execution import build_df
from services import graphicating_data
import pandas as pd
from datetime import datetime
from services.parsing_execution import get_area, is_areas_list


@click.group()
def run():
    pass


@run.command()
@click.argument('area', required=True)
def start_execution(area):
    start = datetime.now()
    now = start.strftime('%d-%m-%Y')
    list_area = get_area(area)
    is_list = is_areas_list(list_area)
    df_global = pd.DataFrame()
    if is_list:
        for area_item in list_area:
            eq_area = PROV_DICT[area_item]
            LOGGER.info(
                'Starting execution for area: {}'.format(eq_area))
            df_temp = build_df(eq_area)
            if df_temp is not None:
                df_global = df_global.append(df_temp, ignore_index=True)
        area = 'global'
    else:
        eq_area = PROV_DICT[area]
        LOGGER.info(
            'Starting execution for area: {}'.format(eq_area))
        df_temp = build_df(eq_area)
        if df_temp is not None:
            df_global = df_global.append(df_temp, ignore_index=True)
    df_global.to_csv('{}_{}_{}.csv'.format(APP_CONFIG['results_folder'], area,
                                           now), encoding='cp1252', sep='|')
    if APP_CONFIG['plot_data']:
        graphicating_data.create_graph()
    LOGGER.info('Completed the process in {} seconds'.format(
        datetime.now()-start))


if __name__ == '__main__':
    run()
