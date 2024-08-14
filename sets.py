#sets are well defined collection of objects which are non repeatable,unordered collection and sets are immutable datatypes
s={2,3,4,2,4,5,6,7,19}
# print(s)
# info={"carla",11,8.5,False,12}
# print(info)
# sa=set() #empty set
# print(type(sa))
# print(s.union(info))
# print(s.intersection(info))
# s.update(info)
# print(s)
# print(s.symmetric_difference(info)) #(aUb)-(aNb)
# print(s.difference(info)) #elements in original set which are not present in later sets
# print(s.isdisjoint(info))
s2={2,3,4}
if 2 in s2:
    print("2 is present")
else:
    print("2 is absent")
# print(s.issuperset(s2))
# print(s2.issubset(s))
# s2.add(5) #adds single item update adds multiple items
# print(s2)
# item=s2.pop() #randomly pops any items from the set
# print(item)
# del s2 #deles whole set
# s2.clear() #clears all elements from the set keeping the structure intact
# print(s2)