import collections
from re import T   
def concatenationsSum(a):
    # sum = 0
    # for i in range(len(a)):
    #     for j in range(i,len(a)):
    #         prod = str(a[i]) + str(a[j])
    #         sum += int(prod)
    # return sum
    tot = 0
    dic = collections.defaultdict(int)
    for i in range(len(a)):
        _str = str(a[i])
        n = len(_str)
        dic[n]+=1
    
    for i in  range(len(a)):
        for k,v in dic.items():
            tot+=a[i]*(v*pow(10,k))
        tot+=(a[i]*len(a))
    return tot
print(concatenationsSum([10,2]))