import calendar

from read_data import Read_Parser

class TempChart(Read_Parser):
    '''SOLVING THE THIRD & FIFTH PART OF TASK 1'''

    def __init__(self, dataset, date):
        self.dataset = dataset
        self.date = date 
        

    def days_in_month(self, month):
            '''finding out the number of day in a specific month, used for the loop for the chart'''
            days_in_month = 0
            
            if month == "2": return '28'
            elif month in ['4','6','9','11']: return '30'
            elif month in ['1','3','5','7','8','10','12']: return '31'
            else:
                print("invalid entry")
                return ""
                 

    def temp_chart_calc(self, line):
            '''calculating the bar charts variables '''
            month = self.date[5:]
            year = self.date[:4]
            check = 0
            days_in_month = self.days_in_month(month)
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
                        min_temp_sign = ""
                        max_temp_sign = ""
                        
                        if self.dataset["Min TemperatureC"][i] == None and self.dataset["Max TemperatureC"][i] == None:
                            min_temp_sign = "NO RECORD"
                            max_temp_sign = "NO RECORD"
                            
                        elif self.dataset["Max TemperatureC"][i] == None:
                            max_temp_sign = "NO RECORD"
                            min_temp_sign, max_temp_sign = self.chart_elements("Min TemperatureC", i, min_temp_sign, max_temp_sign)
                        elif self.dataset["Min TemperatureC"][i] == None:
                            min_temp_sign = "NO RECORD"
                            max_temp_sign, min_temp_sign = self.chart_elements("Max TemperatureC", i, max_temp_sign, min_temp_sign)
                        else:
                            max_temp_sign, min_temp_sign = self.chart_elements("Max TemperatureC", i, max_temp_sign, min_temp_sign)
                            min_temp_sign, max_temp_sign = self.chart_elements("Min TemperatureC", i, min_temp_sign, max_temp_sign)

                       
                        self.print_chart( line, j, max_temp_sign, min_temp_sign, i)

                        j = j + 1
                        break



    def chart_elements(self,colume_name, i, temp_sign, temp_sign2):
        temp = self.dataset[colume_name][i] 

        if temp_sign != "NO RECORD" or temp_sign2 != "NO RECORD":               
            if int(self.dataset[colume_name][i]) < 0: 
                temp = temp[1:]
                for k in range (int(temp)): temp_sign2 = temp_sign2 + " "
                                
        for k in range (int(temp)): temp_sign = temp_sign + "+"

        return temp_sign, temp_sign2



    def print_chart(self, line, j, max_temp_sign, min_temp_sign, i):
        '''the unique printing statment for task 1 part.3'''
        if line == 1:
            print(j, f"\033[91m {max_temp_sign}\033[00m", "" if self.dataset["Max TemperatureC"][i] == None else self.dataset["Max TemperatureC"][i] + "C")
            print(j, f"\033[94m {min_temp_sign}\033[00m", ""if self.dataset["Max TemperatureC"][i] == None else self.dataset["Max TemperatureC"][i] + "C")  
            print("\n")   
        else:
            '''the unique printing statment for task 1 part.5'''
            print(j, f"\033[91m {max_temp_sign}\033[00m\033[94m {min_temp_sign}\033[00m"
                , ""if self.dataset["Max TemperatureC"][i] == None else self.dataset["Max TemperatureC"][i] + "C"
                , ""if self.dataset["Max TemperatureC"][i] == None else self.dataset["Max TemperatureC"][i] + "C")  
            print("\n")

    