sen=input("enter the sentence:")
word=sen.split()
freq={}
for w in word:
    if w in freq:
        freq[w]+=1
    else:
        freq[w]=1
print(freq)