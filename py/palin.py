word=(input("enter the string:"))
if word==word[::-1]:
    print(f"the word {word} is a palindrome")
else:
    print(f"the word {word} is not a palindrome")