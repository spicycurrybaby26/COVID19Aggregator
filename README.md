COVID-19 Vaccination Sites Aggregator

Our project is a program which enables the user easily access necessary updates regarding Covid-19 vaccination in Maryland. The program would read through the API, store in the data attribute, extract the data from the attribute, then get the user input and finally filter the data attribute based on the input. Since the program is limited to the state of Maryland, it used Maryland.gov as API resource. 

How to run the program from the command line: 
    Save the files vacInfo3.py and GUI.py in the same folder on your computer. In your terminal, open up the directory in which the vacInfo script and GUI script is saved. 
    
    Enter python3 GUI.py into command line 

How to use the program/how to interpret the output of the program: 
    (1)When you run the program from the command line, a graphical interface will pop up on your screen. The interface window fill be titled “Maryland Vaccination Sites Lookup 
    (2)The interface will have two search filter options. Click on the option you would like to filter by. 
    (3)A drop down menu will appear in which you can choose either the type of site or the county you would like to filter your results by 
    (4)Then a search button will appear. Click the search button. 
    (5)Then do File >> Save on your computer. This saves the results in a csv to your computer. The results will be saved in a csv (“sites.csv”) in the directory you ran GUI.py in. 
    (6)Open up the sites.csv file to see a filtered list of sites with their corresponding name, address, phone number, website url, site type, and county.

Alternate Option: run vacInfo3.py from command line
    (1)When you run the program from the command line, it will ask to enter a filter you would like to filter your results by (enter in either “county” or “site type”)
    (2)If you entered county as a filter, enter the name of one of the following counties (must follow proper capitalization): 
        List of counties in API: Allegany, Anne Arundel, Baltimore, Baltimore City, Calvert, Carrol, Caroline, Cecil, Charles, Dorchester, Frederick, Garrett, Harford, Howard, Montgomery, Kent, Queen Anne’s, Prince George’s, Somerset, St. Mary’s, Talbot, Washington, Worcester, Wicomico
    (3)If you entered site type as a filter, enter the type of site from one of the following options: 
        List of site types in API: Hospital, Hospital - JHU, Hospital - Medstar, Hospital - UMMS, Local Health Department, Hospital - Adventist Healthcare, Pharmacy, Mass Vaccination
    (4)The program will then print out “Thank you, please check your directory for file”. The csv file with the filtered results will be saved to the folder you ran the program in. The name of the excel file is sites.csv
    (5)Open up the sites.csv file to see a filtered list of sites with their corresponding name, address, phone number, website url, site type, and county. 

Annotated Bibliography: 
“All Maryland Vaccination Sites.” Maryland.gov, 13 May 2021, 
    coronavirus.maryland.gov/datasets/all-maryland-vaccination-sites-1/geoservice? geometry=-82.760%2C37.447%2C-71.762%2C40.437.

We used the Maryland Vaccination sites API to gain access to data on vaccination sites in Maryland. This API is updated daily, which allows our program to generate accurate and current data. The information provided for each site includes the site name, county, address, phone number, site type, walk-in hours and much more. The information is submitted by each vaccination site themselves, thus we can trust that this information will be accurate. 

Unit Testing Explanation

This program's functions are entirely based on manual input and therefore cannot be unittested. 
An explanation on how to test each method can be found below:

vacInfo3.py:
- fill_data(): In order to test the function, the user would need to confirm that the csv file
generated matches the expected output. More detailed testing can be done in the program by
running the fill_data function on an instance of the APIReader and printing the results.
- get_output(): In order to test the function, the user would need to confirm that the csv file
generated matches the expected output. More detailed testing can be done in the program by
running the get_output() function on an instance of the Extractor and printing the results.
- get_file(): In order to test the function, the user would need to confirm that the csv file
exists and generated matches the expected output.