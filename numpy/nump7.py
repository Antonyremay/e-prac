import numpy as np
print(a:=np.random.randint(1,100,36).reshape(6,6))
print(rsum:=a.sum(axis=1))
print(cmean:=a.mean(axis=0))
print(f"the maximum  value is {(tmax:=a.max())}")
row,col=np.unravel_index(a.argmax(),a.shape)
print(F"the index position is in row {row} and column {col}")