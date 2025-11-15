import numpy as np

a = np.array([1, 2, 3])
print(a)
print(a.shape)         # (3,)

b = np.expand_dims(a, axis=0)
print(b)
print(b.shape)         # (1, 3)
a = np.array([[[1, 2, 3]]]) 
print(a) 
print(a.shape)        # (1, 1, 3)

b = np.squeeze(a)
print(b)
print(b.shape)        # (3,)
c= np.array([1,2,3])
d= np.array([4,5,6])
print(np.hstack((c,d)))
print(np.vstack((c,d)))
print(np.concatenate((c,d)))
np.random.seed(10)
print(i:=np.random.randint(1,50,5))
print(np.clip(i,10,20))