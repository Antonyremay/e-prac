def liss(n):
    return [i for i in range(1,n+1)]
n=int(input("enter the range for the numbers:"))
print(liss(n))
sum=0
mi=liss(n)[0]
ma=liss(n)[0]
for i in liss(n):
    sum=sum+i
for i in liss(n):
    if i<mi:
        mi=i
    if i>ma:
        ma=i
print("Sum:",sum)
print("Min:",mi)
print("Max:",ma)