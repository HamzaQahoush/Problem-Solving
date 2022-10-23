def number_of_ways(s):
    L=len(s)
    res=0
    for i in range(1,L-1): 
        for j in range(i+1,L):
            a=s[0:i]
            b=s[i:j]
            c=s[j:L]
            if (a+ b) != (b+c) and (b+c) != (c+a)  and (a+ b) != (c+a):
                res+=1
    return res
s = "xzxzx"
print (number_of_ways(s))
