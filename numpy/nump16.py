import numpy as np
print(a:=np.random.randint(1,100,25).reshape(5,5))
print(b:=np.random.randint(1,100,25).reshape(5,5))
print(m:=a@b)
print(mu:=np.dot(a,b))
print(mul:=np.matmul(a,b))
if np.array_equal(m, mu) and np.array_equal(mu, mul):
    print(True)
else:
    print(False)