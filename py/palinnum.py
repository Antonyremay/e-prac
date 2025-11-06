num=int(input("enter the number:"))
temp=num
rev=0

while num>0:
    dig=num%10
    rev=rev*10+dig
    num//=10

if rev==temp:
    print(f"the num {temp} is a palindrome")
else:
    print(f"the num {temp} is not a palindrome")