def fibo(n):
    if n<=0:
        return "invalid input"
    elif n==1:
        return 0
    elif n==2:
        return 1;
    else:
        return fibo(n-1)+fibo(n-2)
def print_fibo(n):
    return [fibo (i) for i in range(1,n+1)]
def main():
    n=int(input("Enter the number of trems:"))
    print("Fibonacci sequence:",print_fibo(n));
if __name__=="__main__":
    main()