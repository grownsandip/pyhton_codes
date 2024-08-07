class Test:
    def __init__(self,val):
        self._val=val
          
    def show(self):
        print(f"The value is:{self._val}")

    @property  #acts as a getter(basically we are creating a attribute of an object of class Test)
    def ten_val(self):
        return 10*self._val
    
    @ten_val.setter #setter of the ten_val attribute
    def ten_val(self,new_val):
        self._val=new_val

    

obj=Test(10)
#obj.ten_val=32 we cannot directly modify the attribute value of objects which is why we have setter
obj.ten_val=90
print(obj.ten_val)
obj.show()