class Fact:
   def __init__(self,num):
       self.num=num
   def calculate(self):
       if self.num<0:
           raise ValueError("Not defined for negative numbers")
       return self.factorial(self.num)
   def factorial(self,n):
       if n==0 or n==1:
           return 1
       return n*self.factorial(n-1)
    
def main():
    try:
        num=int(input("Enter a number:"))
        calculator=Fact(num)
        result=calculator.calculate()
        print(f"The factorial of the number is:{result}")
    except ValueError as e:
        print(f"Error: {e}")
if __name__=="__main__":
    main()