import numpy as np
a=np.random.randint(1,1000,25).reshape(5,5)
a90=a.T[:,::-1]
a_90=a.T[::-1,:]
a180=a.T[::-1,::-1]
t=a.T
print(f"the original is: \n{a}")
print(f"the a90 is: \n{a90}")
print(f"the a_90 is: \n{a_90}")
print(f"the a180 is: \n{a180}")
print(f"the transpose is: \n{t}")