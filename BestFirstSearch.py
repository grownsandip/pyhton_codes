import heapq
ROWS=10
COLS=10
Graph=[
    [0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0],
    [0,0,1,0,1,0,0,0,0,0],
    [0,0,1,0,0,0,1,1,0,0],
    [0,0,1,0,1,0,1,0,0,0],
    [0,0,0,0,0,0,0,0,1,0],
    [0,1,1,0,1,0,1,0,1,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0]
]
def heuristics(node,goal):
    return abs(node[0]-goal[0])+abs(node[1]-goal[1]) #manhatten distance as heuristics |x1-x2|+|y1-y2|

def best_first_search(start,goal):
    open_list=[]
    heapq.heappush(open_list,(0,start))
    came_from={}
    cost_so_far={start:0}
    while open_list:
        _,current=heapq.heappop(open_list)
        if current==goal:
            break
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]: #searching in all 4 directions
            next_node=(current[0]+dx,current[1]+dy)
            if(0<=next_node[0]<ROWS and 0<=next_node[1]<COLS and Graph[next_node[0]][next_node[1]]==0):
                new_cost=cost_so_far[current]+1 #updating cost
                if next_node not in cost_so_far or new_cost<cost_so_far[next_node]:
                    cost_so_far[next_node]=new_cost #set new cost of next_node so far
                    priority=heuristics(next_node,goal) #find the heuristics
                    heapq.heappush(open_list,(priority,next_node)) #push the next_node and heuristics in queue
                    came_from[next_node]=current #update the parent for next_node
    current=goal
    path=[]
    while current!=start:
        path.append(current)
        current=came_from[current]
    path.append(start)
    path.reverse()
    return path

def main():
    start=(0,0)
    goal=(5,5)
    path=best_first_search(start,goal)
    print(path)   
    
if __name__=="__main__":
    main()