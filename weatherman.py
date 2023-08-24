import os
import sys
import calendar


class Read_parser:
    def __init__(self):
        self.dataset = {}

    def parse_file(self,dir_path):

        file_names = os.listdir(dir_path)
        txt_files = [file for file in file_names if file.endswith(".txt")]
        count = 0
        v = 0

        for txt_file in txt_files:
            file_path = os.path.join(dir_path, txt_file)
            with open(file_path, "r") as file:
                data = file.readlines()
                
            for line in data:
                line_lis = line.strip().split(',')
                
                if count == 0:
                    count = count + 1
                    labels = []
                    for i in line_lis:
                        labels.append(i)
                        self.dataset[i] = []
                        
                    
                else:
                    for i in range(len(line_lis)):
                        if line_lis[i] == "PKT":
                            line_lis[i] = "PKST"
                        if line_lis[i] not in labels:
                            
                            if line_lis[i] == '':
                                self.dataset[labels[i]].append(None)
                            else:
                                self.dataset[labels[i]].append(line_lis[i])                   
        
        return self.dataset

    def years(self,years):
        
        max_temp = 0
        min_temp = 0
        humidity = 0
        check = 0

        for i in range(len(self.dataset["PKST"])):
            if years in self.dataset["PKST"][i].split("-")[0]:
                check = check + 1
        if check == 0:
            print("no record")
            return
        
        #print(len(self.dataset["PKST"]))
        #print(len(self.dataset["Max Humidity"]))

        for i in range(len(self.dataset["PKST"])):
            if years in self.dataset["PKST"][i].split("-")[0]:
                if self.dataset["Max TemperatureC"][i] == None:
                    max_temp = max_temp
                elif int(self.dataset["Max TemperatureC"][max_temp]) < int(self.dataset["Max TemperatureC"][i]):
                    max_temp = i
                if self.dataset["Min TemperatureC"][i] == None:
                    min_temp = min_temp
                elif int(self.dataset["Min TemperatureC"][min_temp]) > int(self.dataset["Min TemperatureC"][i]):
                    min_temp = i
                if self.dataset["Max Humidity"][i] == None :
                    humidity = humidity
                elif int(self.dataset["Max Humidity"][humidity]) < int(self.dataset["Max Humidity"][i]):
                    humidity = i
        
        print("Highest: "+ str(self.dataset["Max TemperatureC"][max_temp])
              + "C on " + str(calendar.month_name[int(self.dataset["PKST"][max_temp].split("-")[1])])
              +" " + str(int(self.dataset["PKST"][max_temp].split("-")[2])))
        
        print("Lowest: "+ str(self.dataset["Min TemperatureC"][min_temp])
              + "C on " + str(calendar.month_name[int(self.dataset["PKST"][min_temp].split("-")[1])])
              +" " + str(int(self.dataset["PKST"][min_temp].split("-")[2])))
        
        print("Humidity: "+ str(self.dataset["Max Humidity"][humidity])
              + "% on " + str(calendar.month_name[int(self.dataset["PKST"][humidity].split("-")[1])])
              +" " + str(int(self.dataset["PKST"][humidity].split("-")[2])))
        
    def month(self,month):
            month = month[5:]
            avg_max_temp = 0
            avg_min_temp = 0
            avg_humidity = 0
            avg_humidity_count = 0
            check = 0

            for i in range(len(self.dataset["PKST"])):
                if month == self.dataset["PKST"][i].split("-")[1]:
                    check = check + 1
            if check == 0:
                print("no record")
                return
            
            #print(len(self.dataset["PKST"]))
            #print(len(self.dataset["Max Humidity"]))

            for i in range(len(self.dataset["PKST"])):
                if month == self.dataset["PKST"][i].split("-")[1]:
                    if self.dataset["Mean TemperatureC"][i] == None:
                        avg_max_temp  = avg_max_temp 
                    elif int(self.dataset["Mean TemperatureC"][avg_max_temp]) < int(self.dataset["Mean TemperatureC"][i]):
                        avg_max_temp = i
                    if self.dataset["Mean TemperatureC"][i] == None:
                        avg_min_temp = avg_min_temp 
                    elif int(self.dataset["Mean TemperatureC"][avg_min_temp]) > int(self.dataset["Mean TemperatureC"][i]):
                        avg_min_temp = i
                    if self.dataset[" Mean Humidity"][i] == None :
                        avg_humidity = int(avg_humidity)
                    else:
                        avg_humidity = int(avg_humidity) + int(self.dataset[" Mean Humidity"][i])
                        avg_humidity_count = avg_humidity_count + 1
            
            print("Highest Average: "+ str(self.dataset["Mean TemperatureC"][avg_max_temp]) + "C")
            
            print("Lowest Average: "+ str(self.dataset["Mean TemperatureC"][avg_min_temp]) + "C" )
            
            print("Average Mean Humidity: "+ str(round(int(avg_humidity)/int(avg_humidity_count))) + "%")
            
    def temp_chart(self,date):
            month = date[5:]
            year = date[:4]
            days_in_month = 0
            max_temp = 0
            min_temp = 0
            check = 0
            print("\n",str(calendar.month_name[int(month)]), year)
            if month == "2":
                days_in_month = '28'
            elif month in ['4','6','9','11']:
                days_in_month = '30'
            elif month in ['1','3','5','7','8','10','12']:
                days_in_month = '31'
            else:
                print("invalid entry")
                

            for i in range(len(self.dataset["PKST"])):
                if year == self.dataset["PKST"][i].split("-")[0]:
                    check = check + 1
            if check == 0:
                print("no record from this year")
                return
            
            #print(len(self.dataset["PKST"]))
            #print(len(self.dataset["Max Humidity"]))
            j = 1
            while j != int(days_in_month) + 1:
                for i in range(len(self.dataset["PKST"])):
                    #print(self.dataset["PKST"][i].split("-")[2], j)
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

                        
                        print(j, f"\033[91m {max_temp_sign}\033[00m", self.dataset["Max TemperatureC"][i] + "C")
                        print(j, f"\033[94m {min_temp_sign}\033[00m", self.dataset["Min TemperatureC"][i] + "C")  
                        print("\n")                
                        j = j + 1
                        break
    def temp_chart_2(self,date):
            
            month = date[5:]
            year = date[:4]
            days_in_month = 0
            max_temp = 0
            min_temp = 0
            check = 0
            print("\n",str(calendar.month_name[int(month)]), year)
            if month == "2":
                days_in_month = '28'
            elif month in ['4','6','9','11']:
                days_in_month = '30'
            elif month in ['1','3','5','7','8','10','12']:
                days_in_month = '31'
            else:
                print("invalid entry")
                

            for i in range(len(self.dataset["PKST"])):
                if year == self.dataset["PKST"][i].split("-")[0]:
                    check = check + 1
            if check == 0:
                print("no record from this year")
                return
            
            #print(len(self.dataset["PKST"]))
            #print(len(self.dataset["Max Humidity"]))
            j = 1
            while j != int(days_in_month) + 1:
                
                for i in range(len(self.dataset["PKST"])):
                    #print(self.dataset["PKST"][i].split("-")[2], j)
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

                        
                        print(j, f"\033[91m {max_temp_sign}\033[00m\033[94m {min_temp_sign}\033[00m"
                              , self.dataset["Min TemperatureC"][i] + "C"
                              , self.dataset["Max TemperatureC"][i] + "C")  
                        print("\n")                
                        j = j + 1
                        break
                        
def main():         
    arg = sys.argv

    dir_path = arg[1]
    if len(sys.argv) == 5 or arg[2] == "-c" or arg[4] == "-a" or arg[6] == "-e":
        if not os.path.exists(dir_path):
            print(f"No file found at: {dir_path}")
            return
    else:
        print("Imporper format used.")
        return
        
    parser = Read_parser()
    dataset = parser.parse_file(dir_path)

    print("\n")
    parser.years(str(arg[3]))

    print("\n")
    parser.month(str(arg[5]))

    print("\n")
    parser.temp_chart(str(arg[7]))

    print("\n")
    parser.temp_chart_2(str(arg[7]))



if __name__ == "__main__":
    main()
    