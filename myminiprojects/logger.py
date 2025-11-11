from datetime import datetime
def log_event(message):
    try:
        with open("logs.txt","a",encoding="utf-8") as f:
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp} {message}\n")
            print("logged successfully")
    except Exception as e:
        print(f" the error is{e} ")
