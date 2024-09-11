#walrus operator evaluates variables as part of larger expression
# foods=list()
# while True:
#     food=input("What food would you like:")
#     if food=="quit":
#         break
#     foods.append(food)
# print(foods)
# with walrus operator
foods=list()
while(food:=input("Enter your food:"))!="quit":
    foods.append(food)
print(foods)