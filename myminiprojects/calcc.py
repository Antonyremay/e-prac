import math
times=int(input("enter the number of times:"))
n=int(input("enter the number:"))
def run(n):
    return n**2, n**3,math.factorial(n)

for i in range (times):
    run(n)

def valid():
    try:
        with open("cal.txt","w",encoding="utf-8") as fol:
            res=[]
            dic={}
            r=run(n)
            res.append(r)
        with open("calout.csv","w") as sh:
            for i in sh:
                sh.write(i)
    except ValueError as v:
        print(v)
valid()