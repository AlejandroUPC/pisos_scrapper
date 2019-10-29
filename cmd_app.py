import click
from commons.prov_dict import PROV_DICT
from configuration.init_config import APP_CONFG, LOGGER
from services.parsing_execution import build_df


@click.group()
def run():
    pass


@run.command()
@click.argument('area', required=True)
def start_execution(area):
    if area == '*':
        LOGGER.warning('Running code for ALL provinces')
        for key in PROV_DICT.keys():
            eq_area = PROV_DICT[key]
            LOGGER.warning(
                'Starting execution for area {}-{}'.format(area, eq_area))
            build_df(eq_area)
    else:
        try:
            eq_area = PROV_DICT[area]
        except Exception as e:
            LOGGER.error(
                'Error trying to get data for abreviation {} - {}'.format(area, e))
        finally:
            LOGGER.warning(
                'Starting execution for area {}-{}'.format(area, eq_area))
            build_df(eq_area)


if __name__ == '__main__':
    run()
