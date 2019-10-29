"""
    The two dictionaries to parse the different attributes of the flat and how to proceed.
"""
BASICDATA_DICT = {'superficieutil': 'NNS',
                  'habitacionamueblada': 'TSS',
                  'numhabitaciones': 'NNS',
                  'numbanos': 'NNS',
                  'estadoconservacion': 'TNS',
                  'gastosincluidosenalquiler': 'TTS'}

INQDATA_DICT = {
    'Número de inquilinos': 'TNS',
    'Edad mínima': 'TNS',
    'Género': 'TNS'}
