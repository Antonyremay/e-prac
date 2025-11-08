import os
f="ivn6.txt"
if not os.path.exists(f):
    print("file doesn't exist")
    choice=input(f"do you want to create {f} file? (y/n):")
    if choice.lower()=='y':
        with open("ivn6.txt","w+",encoding="utf-8") as f:
            words=input("enter any words:")
            f.write(words)
            f.seek(0)
            print(f.read())

else:
    with open("ivn6.txt","r+",encoding="utf-8") as f:
        f.seek(0)
        print(f.read())