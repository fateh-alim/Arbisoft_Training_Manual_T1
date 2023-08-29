import os
import csv


class ReadParser:
    '''creating the parent class containing the base database of weather files'''

    def __init__(self):
        self.dataset = {}

    def database(self):
        return self.database

    def parse_file(self,dir_path):
        ''' combining and converting the weatherfiles data into a single dictionary  '''
        
        file_names = os.listdir(dir_path)
        txt_files = [file for file in file_names if file.endswith(".txt")]
        count = 0

        for txt_file in txt_files:
            file_path = os.path.join(dir_path, txt_file)
            with open(file_path, "r") as file:
                data = csv.reader(file, delimiter=",")
            
                for line in data:
                    
                    if count == 0:
                        count = count + 1
                        labels = []
                        for i in line:
                            labels.append(i)
                            self.dataset[i] = []  
                    else:
                        for i in range(len(line)):
                            if line[i] == "PKT":
                                line[i] = "PKST"
                            if line[i] not in labels:
                                
                                if line[i] == '':
                                    self.dataset[labels[i]].append(None)
                                else:
                                    self.dataset[labels[i]].append(line[i])                   
            
        return self.dataset

