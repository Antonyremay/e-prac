import numpy as np
def coscal(a,b):
    return np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))
    
a=np.random.randint(1,100,5)
b=np.random.randint(1,100,5)
print(coscal(a,b))