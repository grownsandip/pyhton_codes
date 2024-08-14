#enumerate is function that gives us index as well as value
#enumerate packs it as tuple and return the ind,val as a tuple
list=[5,23,43,5,6,32,43,88]
for index,num in enumerate(list):
    if index==3:
        print("There is index 3")