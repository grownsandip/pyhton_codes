def dec_to_bin(num):
    binary=0
    temp=num
    while(temp!=0):
        rem=temp%2
        binary=binary*10+rem
        temp//=2
    return binary

def main():
    num=int(input("Enter the decimal number:"))
    print("The binary representation of the number is:",dec_to_bin(num))
    
if __name__=="__main__":
    main()