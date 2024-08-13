def func1():
    try:
        l=[1,2,3,4]
        i=int(input("Enter a index number:"))
        print(l[i])
        return 1
    except:
        print("some error has occured")
        return 0
    #finally:
        
        print("I am always executed")
print(func1())