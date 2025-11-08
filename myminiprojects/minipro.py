import logging
from datetime import datetime

logging.basicConfig(filename="minipro.log",level=logging.ERROR)
try:
    filena=input("enter the file name:")
    with open (filena,"r") as f:
        print(f.read())

except FileNotFoundError as e:
    logging.error(f"the file {e} never existed and the logging date is {datetime.today()} time is {datetime.now()} ")
    