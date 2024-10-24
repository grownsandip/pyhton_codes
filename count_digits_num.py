def num_dig(num):
    count=0
    temp=num
    while(temp!=0):
        rem=temp%10
        print(rem)
        count=count+1
        temp//=10
    return count
    

def main():
    num=int(input("Enter a number:"));
    print("the number of digits in the provided number is:",num_dig(num))
    
if __name__=="__main__":
    main()