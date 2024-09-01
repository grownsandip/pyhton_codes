class Employee:
    company="APPLE"
    def show(self):
        print(f"The name of the employee is {self.name} and company is {self.company}")
    # def changeComp(cls,newComp): #this changes only the instance not the class company name.
    #     cls.company=newComp
    @classmethod
    def changeComp(cls,newComp): #this changes the class variable here cls is the actual class referenece
        cls.company=newComp

e1=Employee()
e1.name="SANDIP"
e1.show()
e1.changeComp("TESLA")
e1.show()
print(Employee.company)