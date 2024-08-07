#decorators are fuctions that modify other functions
def greet(fx):#defination of decorator fuction that take a function as input
      def mfx():
        print("Good morning")
        fx() #runs the hello function
        print("Thanks for using this function")
      return mfx

@greet #wrapping inside greet decorator
def hello():
    print("HELLO WORLD")

hello()