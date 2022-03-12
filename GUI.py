""" A script that creates a simple Graphical User Interface (GUI) where users can filter the vaccination sites results parsed from official Maryland Covid-19 vaccination sites API.."""
import vacInfo3
import tkinter as tk
from csv import DictWriter
from tkinter import *
           
class GUI:
    """  This class creates Graphical User Interface (GUI) based on data from vacInfo3 APIreader.
    
    Attributes:
        data (JSON data): data obtained from API.
        apiReader (List of dictionaries): 3 list of dictionaries stored from the VacInfo3 fill_data() method.
        app (GUI): backbone to create a start screen.
    """
    def __init__(self): 
        """ 
        Functionality:
            Creates an instance of APIreader class from the vacInfo3 module.
            Calls fill_data() method and stores it to a variable.
            Creates GUI starting screen.
            When County filter button is clicked, execute apply_county_filter() method.
            When Site Type filter button is clicked, execute apply_site_type_filter() method.
        """
        data = vacInfo3.APIreader()
        
        self.apiReader = data.fill_data()
        
        self.app = Tk()
        menubar = Menu(self.app) 
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Save", command=self.get_excel_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.app.quit)
        
        self.app.title("Maryland Vaccination Sites Lookup")
        self.app.geometry("300x200+100+100")
        self.app.resizable(False, False)
        
        label = Label(self.app, text = "Select Search Filter", width = 100, height = 50, bitmap = "questhead", compound = "top")
        label.pack()
        
        self.countyButton = Button(self.app, text = "Country Filter Options", command = self.apply_county_filter)
        self.countyButton.pack()
        
        self.siteTypeButton = Button(self.app, text = "Site Type Filter Options", command = self.apply_site_type_filter)
        self.siteTypeButton.pack()
        
        self.app.config(menu=menubar) 
        self.app.mainloop()
        
    def callback(self, args):
        """ 
        Functionality:
            Creates the Search button and Texts with args variable.
            When Search button is clicked, execute get_output() method.

        Parameters:
            args (str): represents the selected variable from the drop down menu.   
        """
        countySearch = Button(self.app, text = "Search", command = self.get_output)
        countySearch.pack()
        filter = tk.Label(text="")
        filter.pack()
        
        self.output = self.get_output()
        
        filter.configure(text="The selected filter is {}\nPress Search -> File -> Save".format(self.selected.get()))
        
    def apply_county_filter(self):
        """ 
        Functionality:
            Creates the drop down menu with different county variables.
            When variable is selected, execute callback() method.
            
        Side effects:
            Disables countyButton button.
            Disables siteTypeButton button.
        """
        self.countyButton['state']=DISABLED
        self.siteTypeButton['state']=DISABLED
        
        countyList = self.apiReader[1]
        self.selected = tk.StringVar(self.app)
        self.selected.set("Choose your county")
        
        opt = tk.OptionMenu(self.app, self.selected, *sorted(countyList), command = self.callback)
        opt.pack()
        
    def apply_site_type_filter(self):
        """ 
        Functionality:
            Creates the drop down menu with different site type variables.
            When variable is selected, execute callback() method.
            
        Side effects:
            Disables countyButton button.
            Disables siteTypeButton button.
        """
        self.countyButton['state']=DISABLED
        self.siteTypeButton['state']=DISABLED
        
        siteTypeList = self.apiReader[2]
        self.selected = tk.StringVar(self.app)
        self.selected.set("Choose site type")
        
        opt = tk.OptionMenu(self.app, self.selected, *sorted(siteTypeList), command = self.callback)
        opt.pack()
        
    def get_output(self):
        """ 
        Functionality:
            Stores the first variable from the stored fill_data() method.
            Appends the data to a list based on the variable using get() command.
        
        Side effects:
            Modifies output.
        
        Returns:
            List of dictionaries with selected key-value.
        """
        self.data = self.apiReader[0]
        
        output = []
        for item in self.data:
            if item['county'] == self.selected.get():
                output.append(item)
            if item['site type'] == self.selected.get():
                output.append(item)
        return output
        
    def get_excel_file(self):
        """ 
        Functionality:
            Writes CSV file with headers and rows based on the returned values of the output variable.
        """
        with open("sites.csv","w") as file:
            w = DictWriter(file, ("name","address","phone","url","site type","county"))
            w.writeheader()
            w.writerows(self.output)
 
if __name__ == "__main__":
    GUI()