# class Employee:
#     def __init__(self):
#         self.name="Sandip"   #by default varibales and methods are public

# a=Employee()
# print(a.name)

#PRIVATE MEMBERS
# class Employee:
#     def __init__(self):
#         self.__name="Sandip"  # we have made the name as private
        
# obj=Employee()
# #print(obj.__name)
# print(obj._Employee__name) # using this we can also access private members
# print(obj.__dir__()) #name mangling is a concept used to protect private variables from being overwritten 

#PROTECTED MEMEBERS TO BE ACCESS BY CLASS AND SUBCLASSES

class Student:
    def __init__(self):
        self._name="SANDIP" #name is protected
    def _func(self):
        return "SANDIP" #method is protected
class Subject(Student):
    pass

obj1=Student()
obj2=Subject()  # we are able to access both method and variables using objects of class and subclass.
print(obj1._name)
print(obj1._func())
print(obj2._name)
print(obj2._func())