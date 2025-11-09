words=input("Enter the words:")
def check(words):
    return words==words[::-1]
         
def batch():
    try:
        with open("sample.txt","w",encoding="utf-8") as sample:
            sample.write(words)
            

        with open("sample.txt","r",encoding="utf-8") as sam:
            palin=[]
            for word in sam.read().split():
                if check(word):
                    palin.append(word)

        with open("sampali.txt","w",encoding="utf-8")as file:
            result = ", ".join(palin)
            file.write(result)

        print("data loaded")
    except ValueError as v:
        print(f"error:{v}")
batch()
