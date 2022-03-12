import requests 
from csv import DictWriter

class APIreader: 
    """Class for reading through API
    
    Attributes: 
        jfile (json file): file obtained from API 
        data (list): dictionaries for each site 
        countyList (list): dictionaries for each sites' county
        siteTypeList (list): dictionaries for each sites' site type
    """
    
    def __init__(self):
        """Parsing the API from the JSON URL and stores it.""" 
        
        result = requests.get("https://services.arcgis.com/njFNhDsUCentVYJW/arcgis/rest/services/MD_Vaccination_Locations/FeatureServer/4/query?where=1%3D1&outFields=name,fulladdr,scheduling_contact_phone,website_url,site_type,County&outSR=4326&f=json")
        self.jfile = result.json()
    
    def fill_data(self):
        """Fills the data list with name, address, phone, site type and county
            Does not require unit tests, output changes based on manual user input
        
        Side effects: 
            Modifies data attribute 
            Modifies countyList attribute 
            Modifies siteTypeList attribute 
            
        Returns:
            The modified 3 list of dictionaries.
        """  
        data = []
        countyList = []
        siteTypeList = []
        
        i = 0
        for i in range(len(self.jfile["features"])):
            name = self.jfile["features"][i]["attributes"]["name"]
            address = self.jfile["features"][i]["attributes"]["fulladdr"]
            phone = self.jfile["features"][i]["attributes"]["scheduling_contact_phone"]
            url = self.jfile["features"][i]["attributes"]["website_url"]
            site_type = self.jfile["features"][i]["attributes"]["site_type"]
            county = self.jfile["features"][i]["attributes"]["County"]
            items = {"name": name, "address": address, "phone": phone, "url": url, "site type": site_type, "county": county}
            countyDic = {"county": county}
            siteTypeDic = {"site type": site_type}
            data.append(items)
            countyList.append(countyDic)
            siteTypeList.append(siteTypeDic)
            i += 1
            
        countyList = list(set(values for dic in countyList for values in dic.values()))
        siteTypeList = list(set(values for dic in siteTypeList for values in dic.values()))
        
        return data, countyList, siteTypeList
    
class Extractor(): 
    """A class to extract county data from an API reader based on input
    
    Attributes: 
        data (list of dictionaries): list of dictionaries for each site
        input (string): name of county you want information from 
        output (list of dictionaries): list of dictionaries 
            for each site in specified county or site type 
    """ 
    def __init__(self, input):
        """ 
        Functionality:
            Creates an instance of APIreader class.
            Calls fill_data() method and stores it to a variable.
            Receives input variable and creates instance to an object.
        
        Parameter:
            input: string. User input of search filter.
        """ 
        apireader = APIreader()
        all_data = apireader.fill_data()
        self.data = all_data[0]
        
        self.input = input 
        self.output = self.get_output()
        
    def get_output(self): 
        """Filters the output based on whether user chose county or site filter.
            Appends data from data attribute to output list 
            Does not require unit tests, output changes based on manual user input
        
        Side effects:
            Modifies output.
        
        Returns:
            List of dictionaries with selected key-value.
        """
        output = []
        
        for item in self.data: 
            if county_filter == True: 
                if item['county'] == self.input: 
                    output.append(item)
            elif site_filter == True: 
                if item['site type'] == self.input: 
                    output.append(item)
        return output
    
    def get_file(self): 
        """ Writes CSV file with headers and rows based on the returned values of the output variable.
            Does not require unit tests, output changes based on manual user input
            
        Side effects: 
            Creates and saves a csv file to your directory
        """
        with open("sites.csv","w") as file: 
            w = DictWriter(file, ("name","address","phone","url","site type","county"))
            w.writeheader()
            w.writerows(self.output) 

def main(user_input): 
    """Creates instance of Extractor class and passes string variable.
        Calls get_file() method and write an CSV file.
    """
    my_extractor = Extractor(user_input)
    my_extractor.get_file()

if __name__ == "__main__": 
    print("Welcome to MD COVID-19 Vaccine Data Center")
    county_filter = False
    site_filter = False
    filter = input("Enter filter (county or site type): ")
    if filter == "county": 
        county_filter = True
        county = input("Please enter a MD county: ").title()
        main(county)
    elif filter == "site type": 
        site_filter = True 
        site = input("Please enter site type: ").title()
        main(site)
    print("Thank you, please check you directory for file")