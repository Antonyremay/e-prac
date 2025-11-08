import math
def geo(times):
    try:
        filename=input("enter the filename:")
        frq={}
        with open(filename,"r") as file:
            for line in file:
                words=line.split()
                for word in words:
                    word=word.lower()
                    frq[word]=frq.get(word,0)+1
        print(f"the words appears in {frq} ")
    
    except FileNotFoundError:
        print(f"the file {filename} do not exist")
times=int(input("how many times to run:"))
for i in range(times):
    geo(times)
                