# THESE ARE HIGEHR ORDER FUNCTIONS THAT TAKES FUNCTIONS AS ARGUMENTS
from functools import reduce
l=[2,3,4,5,6,7,8]
# cube=lambda x:x*x*x
# #cl=[]
# # for items in l:
# #     cl.append(cube(items))
# # print(cl)

# #SAME THING CAN BE ACHEIVED USING MAP FUNCTION 

# cl=list(map(cube,l))
# print(cl)

# FILTER METHOD
# def filter_func(a):
#     return a>6
# nl=list(filter(filter_func,l))
# print(nl)

#REDUCE METHOD TAKES A PREDICTE AND AN ITERABLE AND PERFORMS OPERATIONS

reduced=reduce(lambda x,y:x+y,l)
print(reduced)