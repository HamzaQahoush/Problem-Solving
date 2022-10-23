def solution(matrix):
    rows=len(matrix) # 1,2,3
    cols = len(matrix[0]) #4
    s=set()
    r=0
    for i in range(rows):
        for j in  range (cols):
            if matrix[i][j] ==0  :
                s.add(j)
            elif matrix[i][j] > 0 and j not in s:
                r+=matrix[i][j]
    return r

m=[[0,1,1,2], 
 [0,5,0,0], 
 [2,0,3,3]]
print(solution(m))