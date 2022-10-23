
def climbStairs(n: int) -> int:
    # if n <=3 : return n
    # else:
    #     return self.climbStairs(n-1)+self.climbStairs(n-2)
    
    if n <=3 : return n
    
    arr=[0]*(n+1)
    arr[1]=1
    arr[2]=2

    for i in range(3,n+1):
        arr[i]=arr[i-1]+arr[i-2]
        
    return arr[n]
        
print(climbStairs(4))