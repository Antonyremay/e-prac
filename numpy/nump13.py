import  numpy as np
a=np.random.randint(1,100,25).reshape(5,5)
print(a)
def swap(a,i,j):
     a[[i,j]]=a[[j,i]]
     return a
try:
        i=int(input("enter the first row number:"))
        j=int(input("enter the second row number:"))
        print(swap(a,i,j))

except Exception as e:
        print(f"the error is {e}")

        
#or
# import  numpy as np
# a=np.random.randint(1,100,25).reshape(5,5)
# print(a)
# a[[0,2]]=a[[2,0]]
# print(a)
