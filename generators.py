#Generators are created each time iterabales are iterated in background,generators basically create value on the fly and donot store them 
def my_generator():
    for i in range(4000):
        yield i
#generators are basically lazy in nature meaning it will give output as per want here 5 times calle d so five values will generate
#and remaining 40000 will not be generated
gen=my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
