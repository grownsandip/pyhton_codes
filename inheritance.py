class Employee:
    def __init__(self,name,id):
        self.id=id
        self.name=name

    def showDetails(self):
        print(f"The details are:{self.name} and {self.id}")

class Programmer(Employee):
    def showlan(self):
        print("The default language is java")

#e1=Employee("SANDIP","E1")
#e1.showDetails()
e2=Programmer("SANDIP","e2")
e2.showlan()
e2.showDetails()