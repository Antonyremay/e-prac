import numpy as np
try:
    row=int(input("enter the number of rows :"))
    col=int(input("enter the number of rows :"))
    tot=row*col
    print(a:=np.random.randint(1,100,tot).reshape(row,col))
    a=a[a>50]
    z=np.sort(a)
    y=z.ravel()
    x=y[:10]
    print(x)
    n=len(x)
    f=[(i,n//i)for i in range(1,int(np.sqrt(n))+1) if n%i==0]
    r,c=f[-1]
    b=x.reshape(r,c)
    print(b)
except Exception as e:
    print(f"your error is {e}")