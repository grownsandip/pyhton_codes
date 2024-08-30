# print(int("123"))  # Converts to 123
# print(float("123.45"))  # Converts to 123.45
# print(str(123))  # Converts to "123"
# print(str(123.45))  # Converts to "123.45"
# print(tuple([1, 2, 3]))  # Converts to (1, 2, 3)
# print(list((1, 2, 3)))  # Converts to [1, 2, 3]
# print(list("hello"))  # Converts to ['h', 'e', 'l', 'l', 'o']
# dict_example = {'a': 1, 'b': 2}
# print(list(dict_example.keys()))  # Converts to ['a', 'b']
# print(tuple(dict_example.values()))  # Converts to (1, 2)

my_dict={'a':1,'b':2,'c':1,'d':2,'e':3,'f':2,'g':2}
freq={}
print(type(freq))
for values in my_dict.values():
    if values in freq:
        freq[values]+=1
    else:
        freq[values]=1
for values,count in freq.items():
    print(f"value{values}appeares in {count} times")