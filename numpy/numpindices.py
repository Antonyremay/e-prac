import numpy as np
a=np.zeros((8,8),dtype=int)
a[1::2,::2]=1
a[::2,1::2]=1
print(a)

# or
# import numpy as np
# n=8
# a=(np.indices((n,n)).sum(axis=0)%2)
# print(a)