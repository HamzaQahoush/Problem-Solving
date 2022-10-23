def minOperations( nums) -> int:
    c=0
    
    for i,v in enumerate(nums[1:],start=1):
        if v <= nums[i-1]:
            n= (nums[i-1]-v) +1 
            nums[i]+=n
            c+=n
    return c
    
print (minOperations(nums = [1,1,1]))

"""
https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/
"""