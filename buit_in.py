# l=[1,2,3]
# print(dir(l)) #gives out all the methods and attributes we can use for a class
class Myclass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
obj=Myclass("sandip",20)
print(obj.__dict__) #gives us all atributes as dictionary

