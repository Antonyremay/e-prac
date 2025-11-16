import numpy as np
row=3
col=3
print(a:=np.random.randint(1,100,(row,col)).reshape(row,col))
print(b:=a.flatten())
print(c:=np.reshape(b,(row,col)))