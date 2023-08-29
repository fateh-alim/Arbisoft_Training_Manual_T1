import calendar

from read_data import Read_Parser

class YearlyCalc(Read_Parser):
    '''SOLVING THE FIRST PART OF TASK 1'''

    def __init__(self,dataset, years):
        self.dataset = dataset
        self.years = years


    def yearly_calc(self, calc_type):
        '''getting the max temp, min temp or avghumidity with the recorded date in a set year'''
        years = self.years
        temp, check, humidity = 0, 0, 0

        for i in range(len(self.dataset["PKST"])):
            if years in self.dataset["PKST"][i].split("-")[0]: check = check + 1
        if check == 0:
            print("no record")
            return

        for i in range(len(self.dataset["PKST"])):
            if years in self.dataset["PKST"][i].split("-")[0]:

                if calc_type == "max_temp": temp = self.max_temp(i, temp)
                elif calc_type == "min_temp": temp = self.min_temp(i, temp)
                elif calc_type == "humidity": humidity = self.humidity(i, humidity)
                else: print("ERROR, incorrect input")

        self.yearly_print(calc_type, [temp, humidity])
    

    def max_temp(self, i, max_temp):
        '''getting the index of maximum temperature and the date in a set year'''
        if self.dataset["Max TemperatureC"][i] == None: max_temp = max_temp
        elif int(self.dataset["Max TemperatureC"][max_temp]) < int(self.dataset["Max TemperatureC"][i]): max_temp = i
        return max_temp


    def min_temp(self, i, min_temp):
        '''getting the index of mminimum temperature and the date in a set year'''
        if self.dataset["Min TemperatureC"][i] == None: min_temp = min_temp
        elif int(self.dataset["Min TemperatureC"][min_temp]) > int(self.dataset["Min TemperatureC"][i]): min_temp = i
        return min_temp
    

    def humidity(self, i, humidity):
        '''getting the index of  maximum humidity and the date in a set year'''
        if self.dataset["Max Humidity"][i] == None : humidity = humidity
        elif int(self.dataset["Max Humidity"][humidity]) < int(self.dataset["Max Humidity"][i]): humidity = i
        return humidity


    def yearly_print(self, calc_type, data_lis):
        if calc_type == "max_temp":
            print("Highest: "+ str(self.dataset["Max TemperatureC"][data_lis[0]])
                + "C on " + str(calendar.month_name[int(self.dataset["PKST"][data_lis[0]].split("-")[1])])
                +" " + str(int(self.dataset["PKST"][data_lis[0]].split("-")[2])))
        elif calc_type == "min_temp":
            print("Lowest: "+ str(self.dataset["Min TemperatureC"][data_lis[0]])
                + "C on " + str(calendar.month_name[int(self.dataset["PKST"][data_lis[0]].split("-")[1])])
                +" " + str(int(self.dataset["PKST"][data_lis[0]].split("-")[2])))
        elif calc_type == "humidity":
            print("Humidity: "+ str(self.dataset["Max Humidity"][data_lis[1]])
                + "% on " + str(calendar.month_name[int(self.dataset["PKST"][data_lis[1]].split("-")[1])])
                +" " + str(int(self.dataset["PKST"][data_lis[1]].split("-")[2])))
        else:
            print("ERROR, incorrect input")