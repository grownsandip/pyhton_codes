def add(a,b):
    print("The sum of two numbers are:",(a+b))
    
def prime(a):
    if(a>1):
        for i in range(2,(a//2)+1):
            if(a%i==0):
                print("The number is not prime")
                break
        else:
            print("The number is prime")
    else:
        print("The number is not prime")
        
def odd_even(a):
    if(a%2==0):
        print("The number is even")
    else:
        print("The number is odd")
        
while(1):
    print("1.ADD?\n2.prime?\n3.odd_even?\n4.Exit?")
    choice=int(input("Enter your choice:"))
    match choice:
        case 1:
            x=int(input("Enter first number:"));
            y=int(input("Enter second number:"));
            add(x,y)
        case 2:
            z=int(input("Enter a number"))
            prime(z)
        case 3:
            z=int(input("Enter a number"))
            odd_even(z)
        case 4:
            print("Program exited")
            break
        case _:
            print("Invalid choice please enter a valid choice")
            