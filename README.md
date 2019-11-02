# Pisos_scrapper

This is a project done during my Master in Data Science in UOC.

It scraps information reagarding the price, among other parameters, for the rooms in all the avaiable regions of the website.

## Requierements

All of the Python requierements needed to run this project can be found under the root folder in the file requierements.txt `pip3 install requierements.txt`.

## Structure

The project is built with the following submodules:

1. Commons: Basic functions or dictionaries of the code that are called multiple times and global variables such as dictionaries for parsing.

2. Configuration: The configuration dictionary, initialzing the configuraiton objects ! **Please take the time and check the parameters before running the code for first time **!.

3. Data access: All the operations regarding the data access for the project, mostly html requests.

4. Output files: All the output folders from the results, such as csv, graphs and log files shall be there.

5. Preprocessing: All the transformations of the data.

6. Services: Congregation of functions to be called from the main cmd.

## Configuration file

Please before running the script read through this section and understand all of the fields on **configuraiton/main_configuratio.py**:

* main_url: Defines the main url where the url's to request are built through the code.

* wait_requests: Boolean value to set if you want a delay between every request.

* second_between_reqs: Seconds to wait between requests, wait_request must be set to True.

* results_folder: Path where the CSVs/graphs/images are saved.

* plot_data: Boolean value to decide if the graphs are made after the all the data is gathered.

* plot_data_file: File to be used to plot the data.



## CMD Execution

The project is structured to be ran from the cmd_app.py file and pass the columns.

The main function is named `start-execution` and it takes as a paramter area.

Area is the shortname for the provinces of Spain where we can gather the data from, all the mapping can be found in commons/prov_dict.py.

The code can be run for all the items in commons/prov_dict.py by setting using the paramter '*'.

Examples:

1. To retrieve all the data from Barcelona: 

	`python cmd_app.py start-execution B`
	
	
2. To retrieve all the data from all the provinces (**warning takes a long time**): 

	`python cmd_app.py *`

## Other comments

* Please in order to avoid saturating the server set the flags to wait between request and a reasonable value in the configuration files.

* The graph functions are thought to work with datasets that contain all of the zones (used * as area).