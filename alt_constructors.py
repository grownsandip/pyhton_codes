#suppose if we are accepting data in constructor in a particular format and data may come in some other format than we can use classmethods as alternative constructor.
class Employee:
    def __init__(self,name,salary,company):
        self.name=name
        self.salary=salary
        self.company=company
    @classmethod
    def asString(cls,str):
        return cls(str.split("-")[0],str.split("-")[1],str.split('-')[2])
        
e1=Employee("Sandip",120000,"Apple") # this is the deafault format
print(e1.name)
print(e1.company)
print(e1.salary)
#suppose now the input is coming as string format "sandip-120000-apple"
str="Sandip-12000-Apple"
# e2=Employee(str.split("-")[0],str.split("-")[1],str.split('-')[2]) #we have to slpit the string and than pass as argumant
e2=Employee.asString(str)
print(e2.name)
print(e2.salary)
print(e2.company)
        