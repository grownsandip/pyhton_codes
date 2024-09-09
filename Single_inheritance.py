class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def make_sound(self):
        print("Sound made by animal")
class Dog(Animal):
    def __init__(self,name,breed): #overriding constructor
        Animal.__init__(self,name,species="Dog")
        self.breed=breed
    def make_sound(self):
        print("Bark")
dog=Animal("Bruno","Dog")
bruno=Dog("tiger","labrador")
bruno.make_sound()
            
        