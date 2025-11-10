import csv
import math
times=int(input("enter the number of times:"))
def run(n):
    return n**2, n**3,math.factorial(n)



try:
        
    res=[]
    for i in range (times):
        n=int(input("enter the number:"))
        square,cube,factoria=run(n)
        res.append({
            "number":n,
            "square":square,
            "cube":cube,
            "factorial":factoria
            })
    with open("calout.csv","w",newline="") as sh:
            writer=csv.DictWriter(sh,fieldnames=["number","square","cube","factorial"])
            writer.writeheader()
            writer.writerows(res)
except ValueError as v:
        print(v)
