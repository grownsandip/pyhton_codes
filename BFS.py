from collections import deque
def bfs(graph,start):
    vis=set()
    queue=deque([start])
    while queue:
        node=queue.popleft()
        if node not in vis:
            print(node,end=" ")
            vis.add(node)
            queue.extend(graph[node])
def main():
    graph={
        'A':['B','C'],
        'B':['D','F'],
        'C':['F'],
        'D':[],
        'F':[]
    }
    bfs(graph,'A')
    
if __name__=="__main__":
    main()