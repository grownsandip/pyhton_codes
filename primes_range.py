def sieve(low,high):
    primes=[True for i in range(high+1)]
    p=2
    while(p*p<=high):
        if (primes[p]==True):
            for mul in range(p*p,high+1,p):
                primes[mul]=False
        p+=1
    
    for i in range(low,high+1):
        if primes[i]:
            print(i)
            
def main():
    low=int(input("Enter a lower bound:"))
    high=int(input("Enter a higher bound:"))
    sieve(low,high)
    
if __name__=="__main__":
    main()