
numb=int(input("enter the number of students:"))
def create(numb):
        with open("studen1.txt","a+",encoding="utf-8") as marksheet:
            name=input("enetr the name of students:")
            marks=input("enter the mark  of the students seperated by comma (,):")
            marksheet.write(f"{name},{marks}\n")
        print("data sucessfully loaded")
for i in range(numb):
    create(numb)
def analy(avg):
    if avg>=80:
        return "A"
    elif avg>=70:
        return"B"
    elif avg>=60:
        return"C"
    else:
        return"D"
    
def cal():
    try:
        with open("studen1.txt","r",encoding="utf-8") as upd:
            mart={}
            for lines in upd:
                line=lines.strip().split(",")
                names=line[0]
                markk=[float(x) for x in line[1:]]
                mart[names]=markk

        result={}
        for names,markk in mart.items():
            avg=sum(markk)/len(markk)
            grade=analy(avg)
            result[names]=(grade,avg)

        with open("grade1.txt","w+",encoding="utf-8") as cpm:
            for name,(grade,avg) in result.items():
                cpm.write(f"{name} : {grade} ({avg:.2f})\n")

    except ValueError as e:
        print(f"its a {e} error")
    except TypeError as f:
        print(f"its a {f} error")
    except FileNotFoundError as c:
        print(f"its a {c} error")
cal()