def solution(a):
    b=[0]*len(a)
    L=len(a)
    if len(a)==1 : return a
    for i in range(L):
        if i+1 >=L:
            b[i] = a[i - 1] + a[i] 
        elif i-1 <0 :
            b[i]=a[i + 1] + a[i] 
        else: 
            b[i] = a[i - 1] + a[i] + a[i + 1]
    return b
a= [4, 0, 1, -2, 3]        
print(solution(a))