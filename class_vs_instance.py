class Employee:
    company="APPLE" #this is a class variable associated with class
    def __init__(self,name):
        self.name=name
        self.raise_amt=0.02
    def showDetails(self):
        print(f"The name of the employee is {self.name} at {self.company} got  a raise amount {self.raise_amt}")
        
        
e1=Employee("SANDIP")
e1.showDetails()
e2=Employee("Pulak")
#e2.raise_amt=50 # instance variable changing 
#e2.company="Samsung" #instance variable changing 
e2.showDetails()

#by default instance variable is searched first and if not present than class variable is given precidense