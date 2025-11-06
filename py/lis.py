lis=list(map(int,input("enter the value of the list:").split()))
print(f"the list is {lis}")
min=lis[0]
ma=lis[0]
for i in lis:
    if min>i:
        min=i
        i+=1
for i in lis:
    if ma<i:
        ma=i
        i+=1
print(f"the minimum value in the lis is {min}")
print(f"the maximum value in the lis is {ma}")