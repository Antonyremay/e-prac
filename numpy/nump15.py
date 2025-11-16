import numpy as np
print(a:=np.random.randint(1,1000,300).reshape(100,3))
print(mea:=a.mean(axis=0))
print(std:=a.std())
print(np.corrcoef(a,rowvar=False))