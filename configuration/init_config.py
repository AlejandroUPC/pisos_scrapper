from configuration.main_configuration import ENV_CONF
import logging
fh = logging.FileHandler(ENV_CONF['log_file'])
fh.setFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
LOGGER = logging.getLogger('pisos_scrapper')
LOGGER.addHandler(fh)
APP_CONFIG = ENV_CONF
