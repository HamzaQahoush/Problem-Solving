"""
https://app.codesignal.com/arcade/intro/level-3/D6qmdBL2NYz49XHwM
"""
def solution(a):
    # for i,n in  enumerate(a): 
    #     for j,k in enumerate(a[i+1:],start=i+1):
    #         if n == -1 : break
    #         if n > k  and n != -1 and k != -1:
    #             t=n # 190
    #             a[i]=k # 170
    #             a[j]=t # 19
    #             n=a[i]
                
    # return a
    
    l = sorted([i for i in a if i > 0])
    for n,i in enumerate(a):
        if i == -1:
            l.insert(n,i)
    return l
        
            # [-1,150,160,190,-1,-1,170,180]

a = [-1, 150, 190, 170, -1, -1, 160, 180]
print(solution(a))
# i = 2 
# j = 3