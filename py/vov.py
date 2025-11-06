word=input("enter the word:")
vow="aeiouAEIOU"
al=[]
count=0
for ch in word:
    if ch in vow:
        al.append(ch)
        count+=1
print(f"the vowels in the word are {al} and the count is {count}")