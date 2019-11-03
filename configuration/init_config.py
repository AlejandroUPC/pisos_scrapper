from configuration.main_configuration import ENV_CONF
import logging
fh = logging.FileHandler('output_files/app_logs.log')
format_logs = logging.Formatter(
    ENV_CONF['logs_format'])
fh.setFormatter(
    format_logs)
logging.basicConfig(
    format=ENV_CONF['logs_format'], level=logging.INFO)
LOGGER = logging.getLogger('pisos_scrapper')
LOGGER.addHandler(fh)

APP_CONFIG = ENV_CONF
