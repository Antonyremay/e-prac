import logging
from datetime import datetime

logging.basicConfig(filename="minipro1.log",level=logging.DEBUG)
try:
    filena=input("enter the file name:")
    with open (filena,"r") as f:
        print(f.read())
        logging.debug(f"the file {filena} logged  time is {datetime.now()} ")
except FileNotFoundError as e:
        logging.error(f"the file {e} does not exist and logged time is {datetime.now()}")