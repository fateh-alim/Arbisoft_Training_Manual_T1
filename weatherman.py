import os
import sys
from read_data import ReadParser
from yearly_calc import YearlyCalc
from monthly_calc import MonthlyCalc
from temp_charts import TempChart

def main():  
    ''' This is he main function to run the code '''   
        
    arg = sys.argv

    dir_path = arg[1]
    if len(sys.argv) == 5 or arg[2] == "-c" or arg[4] == "-a" or arg[6] == "-e":
        if not os.path.exists(dir_path):
            print(f"No file found at: {dir_path}")
            return
    else:
        print("Imporper format used.")
        return
        
    parser = ReadParser()
    dataset = parser.parse_file(dir_path)

    print("\n")
    year_calc = YearlyCalc(dataset, str(arg[3]))
    year_calc.yearly_calc("max_temp")
    year_calc.yearly_calc("min_temp")
    year_calc.yearly_calc("humidity")

    print("\n")
    monthly_year = MonthlyCalc(dataset, str(arg[5]))
    monthly_year.monthly_calc("max_temp")
    monthly_year.monthly_calc("min_temp")
    monthly_year.monthly_calc("humidity")

    print("\n")
    temp_charts = TempChart(dataset, str(arg[7]))
    temp_charts.temp_chart_calc(1)

    print("\n")
    temp_charts.temp_chart_calc(2)



if __name__ == "__main__":
    main()
    