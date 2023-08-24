import calendar

from weatherman import Read_Parser

class Yearly_Calc(Read_Parser):
    '''SOLVING THE FIRST PART OF TASK 1'''

    def __init__(self,dataset, years):
        self.dataset = dataset
        self.years = years

    def max_temp(self):
        '''getting the maximum temperature and the date in a set year'''

        years = self.years
        max_temp = 0
        check = 0

        for i in range(len(self.dataset["PKST"])):
            if years in self.dataset["PKST"][i].split("-")[0]:
                check = check + 1
        if check == 0:
            print("no record")
            return

        for i in range(len(self.dataset["PKST"])):
            if years in self.dataset["PKST"][i].split("-")[0]:
                if self.dataset["Max TemperatureC"][i] == None:
                    max_temp = max_temp
                elif int(self.dataset["Max TemperatureC"][max_temp]) < int(self.dataset["Max TemperatureC"][i]):
                    max_temp = i
                
        print("Highest: "+ str(self.dataset["Max TemperatureC"][max_temp])
              + "C on " + str(calendar.month_name[int(self.dataset["PKST"][max_temp].split("-")[1])])
              +" " + str(int(self.dataset["PKST"][max_temp].split("-")[2])))


    def min_temp(self):
        '''getting the mminimum temperature and the date in a set year'''

        years = self.years
        min_temp = 0
        check = 0

        for i in range(len(self.dataset["PKST"])):
            if years in self.dataset["PKST"][i].split("-")[0]:
                check = check + 1
        if check == 0:
            print("no record")
            return

        for i in range(len(self.dataset["PKST"])):
            if years in self.dataset["PKST"][i].split("-")[0]:
                if self.dataset["Min TemperatureC"][i] == None:
                    min_temp = min_temp
                elif int(self.dataset["Min TemperatureC"][min_temp]) > int(self.dataset["Min TemperatureC"][i]):
                    min_temp = i
                        
        print("Lowest: "+ str(self.dataset["Min TemperatureC"][min_temp])
              + "C on " + str(calendar.month_name[int(self.dataset["PKST"][min_temp].split("-")[1])])
              +" " + str(int(self.dataset["PKST"][min_temp].split("-")[2])))
    

    def humidity(self):
        '''getting the most humid day in a set year'''
        
        years = self.years
        humidity = 0
        check = 0

        for i in range(len(self.dataset["PKST"])):
            if years in self.dataset["PKST"][i].split("-")[0]:
                check = check + 1
        if check == 0:
            print("no record")
            return

        for i in range(len(self.dataset["PKST"])):
            if years in self.dataset["PKST"][i].split("-")[0]:
                if self.dataset["Max Humidity"][i] == None :
                    humidity = humidity
                elif int(self.dataset["Max Humidity"][humidity]) < int(self.dataset["Max Humidity"][i]):
                    humidity = i
        
        print("Humidity: "+ str(self.dataset["Max Humidity"][humidity])
              + "% on " + str(calendar.month_name[int(self.dataset["PKST"][humidity].split("-")[1])])
              +" " + str(int(self.dataset["PKST"][humidity].split("-")[2])))
        