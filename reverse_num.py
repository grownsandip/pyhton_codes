a=int(input("Enter a number:"))
rev=0
while(a!=0):
    rem=a%10
    rev=rev*10+rem
    a//=10
print("reverse of the number is:",rev)