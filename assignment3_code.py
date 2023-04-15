import csv
import matplotlib.pyplot as plt

class Employee:
    """models an Employee record."""
    def __init__(self, first_name, last_name, email, years):
        self.first_name=first_name
        self.last_name=last_name
        self.email = email
        self.years = years

    #TODO1: make this class comparable.
    def __lt__(self, other):
        if self.last_name < other.last_name:
            return True
        elif self.last_name == other.last_name and self.first_name < other.first_name:
            return True
        elif self.last_name == other.last_name and self.first_name == other.first_name and self.years > other.years:
            return True
        return False

    def __eq__(self, other):
        return self.first_name == other.first_name and self.last_name == other.last_name and self.years == other.years

    def __str__(self):
        info_str = f'{self.first_name} {self.last_name} {"email:"} {self.email}' \
                    f' {"years:"} {self.years}' 
        return(info_str)  

class EmployeeDataProcessor:

    def __init__(self, data_list=None):
        self.data_list = []

    #TODO2: implement this method.
    def get_data_list_from_csvfile(self, file_name):
        """This method opens the csv file passed in and 
            creates an Employee object for each row of data
            in the file. It appends each object to a list and 
            returns that list."""
        with open(file_name, 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count > 0:
                    employee_obj = Employee(row[0], row[1], row[2], str(row[3]))
                    self.data_list.append(employee_obj)
                line_count += 1
        return self.data_list



    def initialize(self, file_name):
        self.data_list = self.get_data_list_from_csvfile(file_name)

    def get_data_size(self):
        return len(self.data_list)

    #TODO3: implement this method.
    def get_employee_record(self, first_name, last_name, years):
        """Returns the first Employee object in the data_list that
           matches first_name, last_name, and years.
           Returns None if the record is not found."""
        for employee_obj in self.data_list:
            if (employee_obj.first_name == first_name) and (employee_obj.last_name == last_name) and (int(employee_obj.years) == int(years)):
                return employee_obj
        return None



    #TODO4: implement this method.
    def get_employee_list(self, start, end, sorted=False):
        """ Returns a list of employee object from data_list that fall
            within a specific range as specified by start and end index parameters.
            The value of start can be: 0<= start < end.
            The value of end can be: start < end <= length of data_list.
            An Exception is raised if start and end values do not meet these constraints.
            The list is returned in ascending order if the sorted parameter is True,
            unsorted otherwise (default)."""
        new_data_list = []
        if (0 <= start < end) and (start < end <= len(self.data_list)):
            for i in range(start, end):
                new_data_list.append(self.data_list[i])
        else:
            raise Exception
        if sorted is True:
            new_data_list.sort()
        return new_data_list




    #TODO5: implement this method.
    def get_years_list(self):
        """Returns a list that contains only the years from 
            all records on the data_list."""
        years_list = []
        for i in range(len(self.data_list)):
            years_list.append(int(self.data_list[i].years))
        return years_list


    def plot_emp_years(self):
        """Creates and displays a histogram plot of all of the years
            that employees in data_list have worked."""
        data = self.get_years_list()
        #specify bin start and end points
        bin_ranges = [0,1,2,3,4,5,6,7,8,9,10]
        #create histogram with 4 bins
        plt.hist(data, bins=bin_ranges, edgecolor='black')
        plt.title("Years of Employment")
        plt.xlabel("Years")
        plt.ylabel("Frequency")
        plt.show()   

if __name__=="__main__":
    file_name = "employee_data.csv"
    file_name = "test.csv"
    emp_proc = EmployeeDataProcessor()
    emp_proc.initialize(file_name)
    emp_proc.plot_emp_years()