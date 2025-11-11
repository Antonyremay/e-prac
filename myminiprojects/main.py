from logger import log_event
import time

def run():
    try:
        with open("data.txt","w",encoding="utf-8") as f:
            word=input("eneter the message:")
            f.write(word)
        log_event("file created:data.txt")

        time.sleep(1)
        with open("data.txt","r",encoding="utf-8") as t:
            t.read()
        log_event("filr readed: data.txt")

        time.sleep(1)
        log_event("data pipeline generated sucessfully")
    except Exception as r:
        print(f"{r} as error")
run() 

