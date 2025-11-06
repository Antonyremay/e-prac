import math
def fac(n):
    j=1
    for i in range(1,n+1):
        j*=i
    return j
# n=int(input("enter the Factorial number:"))
# print(fac(n))
count=int(input("count : "))
for i in range(count):
   numb=int(input("Munber PLs = "))
   print(fac(numb))

#or
# def fac(n):
#     if n==0 or n==1:
#       return 1
#     else:
#        return n* fac(n-1 )
# n=int(input("enter the Factorial number:"))
# print(fac(n))  