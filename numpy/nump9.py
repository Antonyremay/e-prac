import numpy as np
print(a:=np.random.randint(1,100,25).reshape(5,5))
b=a.copy()
np.fill_diagonal(b,99)
print(b)