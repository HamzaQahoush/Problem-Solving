def arrayChange(nums):
    # c=0

    # for i,k in  enumerate (nums[1:],start=1):       
    #     while nums[i] <= nums[i-1]:
    #         nums[i]+=1   #[-1000,0,-1,1]               #  c=1
    #         c+=1
    # return c
    
    # o(n)
    c=0            
    for i in range(len(nums)-1):
        if nums[i] >= nums[i+1] :
            diff= nums[i]+1 - nums[i+1]
            nums[i+1]= nums[i]+1
            c+=diff
    return  c

nums=[-1000, 0, -2, 0]
print(arrayChange(nums))

"""
https://app.codesignal.com/arcade/intro/level-4/xvkRbxYkdHdHNCKjg
"""