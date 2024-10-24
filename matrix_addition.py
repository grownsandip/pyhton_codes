def add(mat1,mat2):
    res=[]
    for i in range (len(mat1)):
        for j in range (len(mat1[0])):
            res.append(mat1[i][j]+mat2[i][j])
    return res
    
    
def main():
    mat1=[[1,2,3],[3,2,1]]
    mat2=[[1,2,3],[3,2,1]]
    print(add(mat1,mat2))
if __name__=="__main__":
    main()