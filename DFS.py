def dfs(graph,node,Vis=None):
    if Vis is None:
        Vis=set()
    if node not in Vis:
        print("Node",node)
        Vis.add(node)
        for nbr in graph[node]:
            dfs(graph,nbr,Vis)
    
def main():
    graph={
        'A':['B','C'],
        'B':['D','F'],
        'C':['F'],
        'D':[],
        'F':[]
    }
    dfs(graph,'A')
if __name__=="__main__":
    main()