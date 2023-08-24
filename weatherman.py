import os
import sys
import calendar

class Read_Parser:
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

