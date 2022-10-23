def setZeroes( matrix) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    R= len(matrix)
    C= len(matrix[0])
    
    r_set= set()
    c_set=set()
    
    for i in range(R):
        for j in range(C):
            if matrix[i][j]==0:
                r_set.add(i)
                c_set.add(j)
    for i in range(R):
        for j in range(C):
            if i in r_set or j in c_set :
                matrix[i][j]=0

matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(setZeroes(matrix))