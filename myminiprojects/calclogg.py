import logging 
from datetime import datetime
def mess(operation):
    try:
        with open ("loggcal.txt","a",encoding="utf-8") as calc:
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            calc.write(f"{timestamp} {operation}\n")
            
            

    except Exception as e:
        print(f" the error is {e}")
mess("calculation is beginning")
