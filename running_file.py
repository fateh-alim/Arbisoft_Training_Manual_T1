import os
import sys
import calendar
from weatherman import Read_Parser
from yearly_calc import Yearly_Calc
from monthly_calc import Monthly_Calc
from temp_charts import Temp_Chart

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
        
    parser = Read_Parser()
    dataset = parser.parse_file(dir_path)

    print("\n")
    year_calc = Yearly_Calc(dataset, str(arg[3]))
    year_calc.max_temp()
    year_calc.min_temp()
    year_calc.humidity()

    print("\n")
    monthly_year = Monthly_Calc(dataset, str(arg[5]))
    monthly_year.max_temp()
    monthly_year.min_temp()
    monthly_year.humidity()

    print("\n")
    temp_charts = Temp_Chart(dataset, str(arg[7]))
    temp_charts.temp_chart_calc(1)

    print("\n")
    temp_charts.temp_chart_calc(2)



if __name__ == "__main__":
    main()
    