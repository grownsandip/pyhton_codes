def tower(n,source,aux,target)->int:
    if n==1:
        print(f"Move disk1 from {source} to {target}")
        return 
    tower(n-1,source,target,aux)
    print(f"Move disk {n} from {source} to {target}")
    tower(n-1,aux,source,target)
def main():
    n=int(input("Enter number of disk:"))
    tower(n,'A','B','C')

if __name__=="__main__":
    main()