#static methods are methods of complex calculations that we want to ship with the class
class My:
    def __init__(self,num):
        self.num=num
        
    def addToNum(self,n):
        self.num=self.num+n
    @staticmethod
    def add(a,b):
          return a+b
      
obj=My(5)
# print(obj.num)
# obj.addToNum(3)
# print(obj.num)
print(My.add(3,2)) #static methods are not associated to class
