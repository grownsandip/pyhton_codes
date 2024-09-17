#tuples are immutable datatypes order collections of data items they can store multiple varibales in single
tup=(1,2,3,4,5,6,6,"string",True)
print(tup,type(tup))
print(tup[0])
print(tup[1])
print(tup[-2])
if "string" in tup:
    print("yes it exists")
    
#we can also do slicing in tuple which returns a new tuple
# tup2=tup[1:5]
# print(tup2)
# print(tup.count(6)) #returns number of occurences
# print(tup.index(6)) #returns the index of first occurance
# we can convert tuple into list and perform ll list operations on reconvert into tuple
#we can concat two tuples
tup1=(1,2,3,4,5)
tup2=(6,7,8,9,10)
print(tup1+tup2)