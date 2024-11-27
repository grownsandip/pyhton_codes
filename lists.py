marks=[10,5,6,"sandip",True] #list allows multiple datatypes in single list
marks.append("hello")
print(marks)
print(marks[-3])# negetive indexing works
print(marks[len(marks)-3]) #convert negative index to positive
print(type(marks))
if "san" in "sandip":
    print("yes")
else:
    print("no")
    
print(marks[:])
print(marks[::])
print(marks[2:])
print(marks[1:5])
print(marks[1:6:2]) #jumping index by 2

#list comprehension creating a list on the fly
list=[i*i for i in range(10) if i%2==0]
print(list)