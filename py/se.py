s={1,2,3,3,3,66,88,34,3,3,3,3,332,7,8,9}
l=set([4,5,6,34,2,5,8,9,22,])
print(s|l)#union
print(s&l)#intersection
print(s^l)
s.remove(88)
print(s)