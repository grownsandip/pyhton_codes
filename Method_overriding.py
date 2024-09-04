class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y
class Circle(shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius)
    def area(self):  #method overriding
        return 3.14*super().area()
    
sq=shape(4,4)
print(sq.area())
cir=Circle(4)
print(cir.area())