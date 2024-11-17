#this program demonstartes class inside a class or nested classes
class Person:
    def __init__(self):
        self.name="Ram"
        self.db=self.Dob()
        
    def display(self):
        print(f"The name of the person is:{self.name}")
    class Dob:
        def __init__(self):
            self.dd=10
            self.mm=2
            self.yy=2002
        def display(self):
            print(f"The date of birth is:{self.dd}/{self.mm}/{self.yy}")
def main():
    P=Person() #object of Person class
    P.display()
    i=Person().Dob() #object of inner class
    i.display()
if __name__=="__main__":
    main()