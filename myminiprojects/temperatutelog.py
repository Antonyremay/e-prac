import random
from datetime import datetime
times=int(input("enter the number of times that tha temperature needed to be checked:"))
def tempcal():
        with open("temp.txt","w",encoding="utf-8") as fill:
            for i in range(times):
                tem=random.uniform(0,100000)
                fill.write(f"{tem:.2f}\n")
            print("temperatures stored")
tempcal()
def convert():
    faren_values=[]
    try:
            with open("temp.txt","r",encoding="utf-8") as temp_sheet:
                for line in temp_sheet:
                    num = ''.join(ch for ch in line if (ch.isdigit() or ch == '.'))
                    if num:
                        try:
                            faren_values.append(float(num))
                        except ValueError:
                           pass
                
            fahrenheit_values = [(i * 9/5) + 32 for i in faren_values]
            min_temp=min(fahrenheit_values)
            max_temp=max(fahrenheit_values)
            with open("temperature.txt","w+",encoding="utf-8") as res_sheet:
                for i in fahrenheit_values:
                      res_sheet.write(f"the farenheit degree is {i}\n")
                res_sheet.write(f"the minimum degree is {min_temp}\n")
                res_sheet.write(f"the maximum degree is {max_temp}\n")
                res_sheet.write(f"the logged time is {datetime.today()}")
    except TypeError as e:
         print(f"typeerror:{e}")
    except AttributeError as a:
         print(f"error is {a}")

convert()