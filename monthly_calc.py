
from weatherman import Read_Parser

class Monthly_Calc(Read_Parser):
    '''SOLVING THE SECOND PART OF TASK 1'''
        
    def __init__(self,dataset,date):

        self.dataset = dataset
        self.date = date

    def max_temp(self):
            '''getting the Average maximum temperature in a set month'''

            month = self.date[5:]
            avg_max_temp = 0
            check = 0

            for i in range(len(self.dataset["PKST"])):
                if month == self.dataset["PKST"][i].split("-")[1]:
                    check = check + 1
            if check == 0:
                print("no record")
                return

            for i in range(len(self.dataset["PKST"])):
                if month == self.dataset["PKST"][i].split("-")[1]:
                    if self.dataset["Mean TemperatureC"][i] == None:
                        avg_max_temp  = avg_max_temp 
                    elif int(self.dataset["Mean TemperatureC"][avg_max_temp]) < int(self.dataset["Mean TemperatureC"][i]):
                        avg_max_temp = i
                                
            print("Highest Average: "+ str(self.dataset["Mean TemperatureC"][avg_max_temp]) + "C")
          
        
    def min_temp(self):
            '''getting the Average minimum temperature in a set month'''

            month = self.date[5:]
            avg_min_temp = 0
            check = 0

            for i in range(len(self.dataset["PKST"])):
                if month == self.dataset["PKST"][i].split("-")[1]:
                    check = check + 1
            if check == 0:
                print("no record")
                return

            for i in range(len(self.dataset["PKST"])):
                if month == self.dataset["PKST"][i].split("-")[1]:
                    if self.dataset["Mean TemperatureC"][i] == None:
                        avg_min_temp = avg_min_temp 
                    elif int(self.dataset["Mean TemperatureC"][avg_min_temp]) > int(self.dataset["Mean TemperatureC"][i]):
                        avg_min_temp = i
                    
            print("Lowest Average: "+ str(self.dataset["Mean TemperatureC"][avg_min_temp]) + "C" )
            
    def humidity(self):
            '''calculating the Average mean humidity in a set month'''

            month = self.date[5:]
            avg_humidity = 0
            avg_humidity_count = 0
            check = 0

            for i in range(len(self.dataset["PKST"])):
                if month == self.dataset["PKST"][i].split("-")[1]:
                    check = check + 1
            if check == 0:
                print("no record")
                return

            for i in range(len(self.dataset["PKST"])):
                if month == self.dataset["PKST"][i].split("-")[1]:
                    if self.dataset[" Mean Humidity"][i] == None :
                        avg_humidity = int(avg_humidity)
                    else:
                        avg_humidity = int(avg_humidity) + int(self.dataset[" Mean Humidity"][i])
                        avg_humidity_count = avg_humidity_count + 1
            
            print("Average Mean Humidity: "+ str(round(int(avg_humidity)/int(avg_humidity_count))) + "%")
            