#multiple inheritance is used to create multiple classes in one single class
class Employee:
    def __init__(self,name):
        self.name=name
class Dancer:
    def __init__(self,type):
        self.type=type
class EmployeeDancer(Employee,Dancer):
    def __init__(self,name,type):
        self.name=name
        self.type=type
emp1=EmployeeDancer("Sandip","hiphop")
print(f"{emp1.name} dances {emp1.type} dance")
        