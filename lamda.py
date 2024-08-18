#lamda functions are single line finctions 
def sum(fx,value):
    return 6+fx(value)

ans=lambda x:x*2
#avg=lambda x,y,z:(x+y+z)/3
# print(ans(2))
# print(avg(2,3,4))
#print(sum(ans,3)) #we can also pass lamda functions as a paramter to another function
print(sum(lambda x:x*x,3))