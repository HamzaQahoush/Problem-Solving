
import math
def is_square(n):
    return math.floor(math.sqrt(n))==math.ceil(math.sqrt(n))

def numSquares(n: int) -> int:
    stack=[] # 
    res=[]
    for i in range(1,n+1) : # 
        if is_square(i): 
            stack.append(i)
    currentLevel = stack
    level = 1
    while True:
        nextLevel = set()
        for i in currentLevel:
            for j in stack:
                if i + j == n:
                    return level + 1
                elif i + j < n:
                    nextLevel.add(i + j)
        level += 1
        currentLevel = nextLevel

      
            
            
        
    
    
n = 12
print (numSquares(n))

                                              