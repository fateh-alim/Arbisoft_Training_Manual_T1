from read_data import Read_Parser

class MonthlyCalc(Read_Parser):
    '''SOLVING THE SECOND PART OF TASK 1'''
        
    def __init__(self,dataset,date):
        self.dataset = dataset
        self.date = date


    def monthly_calc(self, calc_type):
            '''getting average max temp, average min temp or average mean humidy based on input in a set month'''
            month = self.date[5:]
            avg_temp, avg_humidity, avg_humidity_count, check = 0, 0, 0, 0
           
            for i in range(len(self.dataset["PKST"])):
                if month == self.dataset["PKST"][i].split("-")[1]: check = check + 1
            if check == 0: 
                print("no record")
                return

            for i in range(len(self.dataset["PKST"])):
                if month == self.dataset["PKST"][i].split("-")[1]:
                    if calc_type == "max_temp": avg_temp = self.max_temp(i, avg_temp)  
                    elif calc_type == "min_temp":  avg_temp = self.min_temp(i, avg_temp) 
                    elif calc_type == "humidity": avg_humidity, avg_humidity_count = self.humidity(i, avg_humidity, avg_humidity_count)    
                    else: print("ERROR, incorrect input")

            self.monthly_print(calc_type, [avg_temp, avg_humidity, avg_humidity_count])
    

    def max_temp(self, i, avg_max_temp):
        '''calculate index for average max temperature'''
        if self.dataset["Mean TemperatureC"][i] == None: avg_max_temp  = avg_max_temp 
        elif int(self.dataset["Mean TemperatureC"][avg_max_temp]) < int(self.dataset["Mean TemperatureC"][i]): avg_max_temp = i    
        return avg_max_temp

        
    def min_temp(self, i, avg_min_temp):
        '''calculate index for average min temperature'''
        if self.dataset["Mean TemperatureC"][i] == None: avg_min_temp = avg_min_temp
        elif int(self.dataset["Mean TemperatureC"][avg_min_temp]) > int(self.dataset["Mean TemperatureC"][i]): avg_min_temp = i
        return avg_min_temp


    def humidity(self, i, avg_humidity,  avg_humidity_count):
        '''calculate index for average mean humidity'''
        if self.dataset[" Mean Humidity"][i] == None :  avg_humidity = int(avg_humidity)
        else:
            avg_humidity = int(avg_humidity) + int(self.dataset[" Mean Humidity"][i])
            avg_humidity_count = avg_humidity_count + 1
        return avg_humidity, avg_humidity_count
    

    def monthly_print(self, calc_type, data_lis):
        '''Printing function'''
        if calc_type == "max_temp":  print("Highest Average: "+ str(self.dataset["Mean TemperatureC"][data_lis[0]]) + "C")
        elif calc_type == "min_temp": print("Lowest Average: "+ str(self.dataset["Mean TemperatureC"][data_lis[0]]) + "C" )
        elif calc_type == "humidity": print("Average Mean Humidity: "+ str(round(int(data_lis[1])/int(data_lis[2]))) + "%")
        else: print("ERROR, incorrect input")