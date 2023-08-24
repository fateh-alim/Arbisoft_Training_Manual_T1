import calendar

from weatherman import Read_Parser

class Temp_Chart(Read_Parser):
    '''SOLVING THE THIRD & FIFTH PART OF TASK 1'''

    def __init__(self, dataset, date):
        self.dataset = dataset
        self.date = date 
        

    def days_in_month(self, month):
            '''finding out the number of day in a specific month, used for the loop for the chart'''

            days_in_month = 0
            
            if month == "2":
                return '28'
            elif month in ['4','6','9','11']:
                return '30'
            elif month in ['1','3','5','7','8','10','12']:
                return '31'
            else:
                print("invalid entry")
                return ""
                 

    def temp_chart_calc(self, line):
            '''calculating the bar charts variables '''

            month = self.date[5:]
            year = self.date[:4]
            check = 0
            days_in_month = Temp_Chart.days_in_month(self.date, month)
            print("\n",str(calendar.month_name[int(month)]), year)

            for i in range(len(self.dataset["PKST"])):
                if year == self.dataset["PKST"][i].split("-")[0]:
                    check = check + 1
            if check == 0:
                print("no record from this year")
                return

            j = 1
            while j != int(days_in_month) + 1:
                for i in range(len(self.dataset["PKST"])):
                    if self.dataset["PKST"][i].split("-")[0] == year and self.dataset["PKST"][i].split("-")[1] == month and self.dataset["PKST"][i].split("-")[2] == str(j):
                        max_temp = self.dataset["Max TemperatureC"][i]
                        max_temp_sign = ""
                        min_temp = self.dataset["Min TemperatureC"][i]
                        min_temp_sign = ""

                        if int(self.dataset["Min TemperatureC"][i]) < 0:
                            min_temp = min_temp[1:]
                            for k in range (int(min_temp)):
                                max_temp_sign = max_temp_sign + " "
                                #min_temp = int(min_temp) + 1
                        if int(self.dataset["Max TemperatureC"][i]) < 0:
                            max_temp = max_temp[1:]
                            for k in range (int(max_temp)):
                                min_temp_sign = min_temp_sign + " "
                                #max_temp = int(max_temp) + 1

                        for k in range (int(max_temp)):
                            max_temp_sign = max_temp_sign + "+"
                        for k in range (int(min_temp)):
                            min_temp_sign = min_temp_sign + "+"

                        if line == 1:
                            Temp_Chart.print_2line(self, j, max_temp_sign, min_temp_sign, i)
                        else:
                            Temp_Chart.print_1line(self, j, max_temp_sign, min_temp_sign, i)
                                        
                        j = j + 1
                        break

    def print_2line(self, j, max_temp_sign, min_temp_sign, i):
        '''the unique printing statment for task 1 part.3'''

        print(j, f"\033[91m {max_temp_sign}\033[00m", self.dataset["Max TemperatureC"][i] + "C")
        print(j, f"\033[94m {min_temp_sign}\033[00m", self.dataset["Min TemperatureC"][i] + "C")  
        print("\n")   

    def print_1line(self, j, max_temp_sign, min_temp_sign, i):
        '''the unique printing statment for task 1 part.5'''

        print(j, f"\033[91m {max_temp_sign}\033[00m\033[94m {min_temp_sign}\033[00m"
               , self.dataset["Min TemperatureC"][i] + "C"
               , self.dataset["Max TemperatureC"][i] + "C")  
        print("\n")

    