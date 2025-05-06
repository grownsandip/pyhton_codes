class Node:
    def __init__(self,value,children=None):
        self.value=value
        self.children=children if children else []
        
def alpha_beta(node,depth,alpha,beta,max_palyer):
    if depth==0 or len(node.children)==0:
        return node.value
    if max_palyer:
        value=-float('inf')
        for child in node.children:
            value=max(value,alpha_beta(child,depth-1,alpha,beta,False))
            alpha=max(alpha,value)
            if alpha>=beta:
                break
        return value
    else:
        value=float('inf')
        for child in node.children:
            value=min(value,alpha_beta(child,depth-1,alpha,beta,True))
            beta=min(beta,value)
            if beta<=alpha:
                break
        return value
            
        
        
if __name__=='__main__':
    root=Node(0)
    root.children=[Node(10),Node(20),Node(30)]
    root.children[0].children=[Node(100),Node(200)]
    root.children[1].children=[Node(300),Node(400)]
    root.children[2].children=[Node(500),Node(600)]
    best_value=alpha_beta(root,2,-float('inf'),float('inf'),True)
    print("best_value:",best_value)