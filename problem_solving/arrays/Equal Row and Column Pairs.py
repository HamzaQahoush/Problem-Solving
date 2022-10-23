from calendar import c
from itertools import count


def equalPairs( grid) -> int:
    dic={}
    count=0
    for i,row in enumerate(grid):
        col=get_col(grid,i)
        if col == row or tuple(col) in dic or tuple(row) in dic:
            count+=1
        dic[tuple(col)]=1
        
    return count

 
        


def get_col(matrix,i):
    return [row[i] for row in matrix] 

grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]

print(equalPairs(grid))