def searchMatrix(matrix, target: int) -> bool:
    N= len(matrix)
    M= len(matrix[0])
       
    c=0
    r=N-1
    while r >= 0 and c < M:
        if matrix[r][c]==target: return True
        if  matrix[r][c] < target:
            c+=1
        else:
            r-=1
    return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
            
print(searchMatrix(matrix,target))