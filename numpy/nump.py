import numpy as np
import random
try:
    print(a:=np.arange(9).reshape(3,3))
    (b:=(a[1,2]))
    print(f"the midddle value is: {b}")
    print(c:=np.random.randint(1,100,50))
    print(f"the mean value is:{c.mean()}\nthe standard deviation is:{c.std()}\n")
    c2=c.reshape(5,10)
    print(c2)
    print(part1:=c2.ravel()[:25].reshape(5,5))
    print(part2:=c2.ravel()[25:].reshape(5,5))
    print(part1*part2)
    less=[int(x) for x in c2.ravel() if x<50]
    print(less)
    print(np.eye(5,dtype=int))
    print(x:=np.arange(0,20,))
    print(np.linspace(1,10,3))
    
    print([int(x) for x in x if x%2==0])
    u=np.arange(1,10).reshape(3,3)
    print(sumd:=np.sum(np.diag(u))) #or np.trace(m) can be used
    print(f:=np.random.randint(0,70,5))
    print(g:=np.random.randint(0,35,5))
    print(np.corrcoef(f,g))
    print(np.corrcoef(f,g)[0,1])
except Exception as e:
    print(f"the error is {e}")
