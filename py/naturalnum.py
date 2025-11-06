import math
num=float(input("enter a number:"))
sum=0
i=1
if num<=0:
    print("your number is not a natural number")
else:
    while i<=num:
        sum=sum+i
        i+=1
print(f"the sum of first {num} natural number is {sum}")
    