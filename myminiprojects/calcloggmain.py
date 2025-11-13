from calclogg import mess

def mat():
    try:
        x=int(input("Enter the first value:"))
        y=int(input("Enter the second value:"))
        op=input("enter the operator:")
        
        if op=='+':
            result= x+y
        if op=='-':
            result=x-y
        if op=='*':
            result=x*y
        if op=='/':
            result=x/y
        if op=='**':
            result= x**y
        
        with open("loggcal.txt","a",encoding="utf-8") as met:
            mess(f"Operation: {x} {op} {y} = {result}")
    except Exception as r:
        print(f"the error is {r}")

        

mat()
print("the calculation is done")


    