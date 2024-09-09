#multilevel inheritance is basically family tree
class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
        
    def Show(self):
        print(f"name:{self.name}")
        print(f"species:{self.species}")
class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")
        self.breed=breed
        
    def Show(self):
        Animal.Show(self)
        print(f"breed:{self.breed}")
class Labrador(Dog):
    def __init__(self,name,color):
        Dog.__init__(self,name,breed="Labrador")
        self.color=color
        
    def Show(self):
        Dog.Show(self)
        print(f"color:{self.color}")

d1=Labrador("Tommy","White")
d1.Show()
    
        
        