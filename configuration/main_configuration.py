from datetime import datetime
now = datetime.now().strftime('%d-%m-%Y')
ENV_CONF = {
    #Global config#
    "main_url": "https://www.pisos.com/",
    "wait_requests": False,
    "second_between_reqs": 5,
    "results_folder": "output_files/",
    # Logging info
    "logs_format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "log_file": "output_files/app_logs.log",
    # Graphs configuration
    "plot_data": True,
    "plot_data_file": "output_files/_global_11-11-2019.csv"
}
