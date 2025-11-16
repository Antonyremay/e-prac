import numpy as np
a=np.random.randint(1,100,25).reshape(5,5)
a=a.astype(float)
norm=(a-a.min())/(a.max()-a.min())
print(f"the original value is : \n{a}")
print(f"the normalized value is : \n{norm}")