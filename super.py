# class Parent:
#     def parentMethod(self):
#         print("This is a parent method")
# class Child(Parent):
#     def childMethod(self):
#         print("This a child Method")
#         super().parentMethod() #super keyword is used to acces the parent method from childe class
        
# childObj=Child()
# childObj.childMethod()

class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang=lang
        
Sandip=Programmer("Sandip","12","Python")
print(Sandip.name,Sandip.id,Sandip.lang)