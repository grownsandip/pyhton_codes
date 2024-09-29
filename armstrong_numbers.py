def gen_armstrong(start,end):
    arm_list=[]
    for num in range(start,end+1):
        temp=num
        sum=0
        power=len(str(num))
        while(temp!=0):
            remainder=num%10
            sum+=remainder**power
            temp=temp//10
            if(num==sum):
                arm_list.append(sum)
    return arm_list

def main():
    start=int(input("Enter start value:"))
    end=int(input("Enter end value:"))
    res=gen_armstrong(start,end)
    print(res)
    
if __name__=="__main__":
    main()