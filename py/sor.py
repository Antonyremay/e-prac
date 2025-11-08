liss=list(map(int,input("enter the value of the list:").split()))
print(f"the list is {liss}")
asc=liss.copy()
dsc=liss.copy()
for i in range(len(liss)):
    for j in range(i+1,len(liss)):
        if asc[i]>asc[j]:
            asc[i],asc[j]=asc[j],asc[i]
        if dsc[i]<dsc[j]:
            dsc[i],dsc[j]=dsc[j],dsc[i]
print("the ascending order is:",asc)   
print("the descending order is:",dsc)

#or
asc2=sorted(liss)
print(f"the ascending order is: {asc2}")
desc2=sorted(liss,reverse=True)
print(f"the descending order is: {desc2}")