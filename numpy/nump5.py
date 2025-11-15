import numpy as np
a=np.arange(11)
n=len(a)
f=[(i,n//i) for i in range(1,int(np.sqrt(n))+1) if n%i==0]
rows,cols=f[-1]
reshaped=a.reshape(rows,cols)
print(reshaped)