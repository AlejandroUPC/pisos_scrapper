import pandas as pd
from configuration.init_config import LOGGER, APP_CONFIG
import matplotlib.pyplot as plt


def create_graph():
    df_data = __load_data_file()
    df_by_loc = __group_by_field(df_data, 'area')
    __plotting_bar_logic(df_by_loc, 'Count', 'Flats per area')
    df_avgs = __group_by_field_and_area(df_data, 'area')
    avg_cols = ['superficieutil', 'Price', 'numbanos', 'numhabitaciones']
    for item in avg_cols:
        __plotting_bar_logic(df_avgs, item, 'Avg {} per area'.format(item))
    pass


def __load_data_file(path_to_data=APP_CONFIG['plot_data_file']):
    df = pd.read_csv(path_to_data, sep='|', encoding='cp1252')
    return df


def __group_by_field(df, field):
    df_groupped = df.groupby([field]).size(
    ).reset_index().rename(columns={0: 'Count'})
    df_groupped.sort_values(by=['Count'], inplace=True, ascending=False)
    return df_groupped


def __group_by_field_and_area(df, field):
    df_groupped = df.groupby([field]).mean().reset_index()
    return df_groupped


def __plotting_bar_logic(df, y_col, name_graph):
    ax = df.sort_values(by=[y_col], ascending=False).plot(
        x='area', y=y_col, kind='bar')
    # ax.title(name_graph)
    fig = ax.get_figure()
    fig.savefig('{}{}'.format(
        APP_CONFIG['results_folder'], name_graph), bbox_inches="tight")
    pass
