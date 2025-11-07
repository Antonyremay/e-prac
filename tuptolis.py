def liis(n):
    return [i for i in range(0,n+1)]
n=int(input("enter the range for the numbers:"))
print(f" the list is: {liis(n)}")
tup=tuple(liis(n))
print("the tuple is:",tup)
lis=list(tup)
print(f"the list is: {lis} ")