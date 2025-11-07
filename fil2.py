with open ("ivn2.txt","w") as file:
    for i in range(1,31):
        file.write(f"{i}\n")
    print("Done")
file.close()

tu=open("ivn2.txt","r")
for i in tu:
    j=int(i.strip())
    if j%2==0:
        print(i)