import logging
from datetime import datetime

logging.basicConfig(filename="minipro1.log",level=logging.DEBUG)

filena=input("enter the file name:")
with open (filena,"r") as f:
    print(f.read())
    logging.debug(f"the file  never existed and the logging date is {datetime.today()} time is {datetime.now()} ")
    