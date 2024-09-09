class Vector:
    def __init__(self,i,j,k):
        self.i=i;
        self.j=j;
        self.k=k;
    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"
    def __add__(self,x): #basically overloades the + operator in python
        return Vector(self.i+x.i,self.j+x.j,self.k+x.k)
    def __mul__(self,X): # this overloads the * functionality
        return Vector(self.i*X.i,self.j*X.j,self.k*X.k)
        
vec1=Vector(1,2,3)
vec2=Vector(3,4,5)
print(vec1)
print(vec2)
vec3=vec1+vec2
vec4=vec1*vec2
print(vec3)
print(vec4)
print(type(vec3))
print(dir())
