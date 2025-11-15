import numpy as np
print(a:=np.arange(1,17).reshape(4,4))
a[1:,2:3]=0
print(a)
row=[2,3,1]
col=[3,1,0]
value=[99,99,99]
a[row,col]=value
print(a)