f=open("IVN.txt","a")
f.write("\n"+"nice to meet you")
print("content stored")
f.close()
with open("IVN.txt","r") as r:
    for i in r:
        print(i)