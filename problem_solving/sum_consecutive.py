"""
write a function that recieve an list and return
the SUM  of equal  numbers.
 sum_consecutive 
[2,2,2,7,3,3,1,2] => [6, 7, 6, 1, 2]
"""

def sum_consecutive(arr):
    stack=[arr[0]]
    for i,n in enumerate (arr[1:],start=1): # n=2/n=2/
        t=arr[i-1] # t = 2 / 2 
        if t==n:  # T / 
            stack[-1]+=n # [4]
        else:
            stack.append(n)
    return stack


print(sum_consecutive(arr=[2,2,2,7,3,3,1,2]))