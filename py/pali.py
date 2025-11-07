def palin(word):
    return True if word==word[::-1] else False

word=input("enter the string:")
print(palin(word))