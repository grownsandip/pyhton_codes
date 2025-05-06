# the problem statement is given two jugs with certain capacities whether it is possible to measure capcity of 
#water with these jugs with some steps where we can fillup a jug,pour water from one jug to another and empty jug supply for water is infinite
from collections import deque
def solution(x,y,z):
    queue=deque([(0,0)])
    #set for storing visited states
    visited=set((0,0))
    while queue:
        jug1,jug2=queue.popleft()
        #check if state is reached
        if jug1==z or jug2==z:
            return True
        #there can be four possible states
        #filling jugs
        next_state=(x,jug2) #fill jug1
        if next_state not in visited:
            queue.append(next_state)
            visited.add(next_state)
        next_state=(jug1,y)#fill jug2
        if next_state not in visited:
            queue.append(next_state)
            visited.add(next_state)
        #pouring from one to another
        #pouring form jug1 to jug2
        next_state=(jug1-min(jug1,y-jug2),jug2+min(jug1,y-jug2))
        if next_state not in visited:
            queue.append(next_state)
            visited.add(next_state)
        #pouring from jug2 to jug1
        next_state=(jug1+min(jug2,x-jug1),jug2-min(jug2,x-jug1))
        if next_state not in visited:
            queue.append(next_state)
            visited.add(next_state)
        #emptying jugs
        #empty jug1
        next_state=(0,jug2)
        if next_state not in visited:
            queue.append(next_state)
            visited.add(next_state)
        #empty jug2
        next_state=(jug1,0)
        if next_state not in visited:
            queue.append(next_state)
            visited.add(next_state)
    return False
        
    
def main():
    x=3
    y=5
    z=4
    if solution(x,y,z):
        print("It is possible to measure")
    else:
        print("It is not possible to measure")
if __name__=="__main__":
    main()