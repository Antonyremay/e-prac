import os
print(os.getcwd())
with open("ivn5.txt","w+",encoding="utf-8") as f:
    f.writelines([" good morning","\n remayy","\n all the best"])
    f.seek(0)
    print(f"the first line is {f.readline().strip()}")
    print(f"the second line is {f.readline().strip()}")
    print(f"the third line is {f.readline().strip()}")