import math
def ans(n):
    return n**2,n**3,math.factorial(n)
        

n=int(input("enter the integer:"))
print(f"the square ,cube and factorial of the number {n} is {ans(n)}")