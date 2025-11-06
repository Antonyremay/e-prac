num=int(input("enter a number:"))
a,b=0,1
for i in range(num):
    a ,b=b,a+b
print(f" the fibbnoci sequence of {num} is { a} ")