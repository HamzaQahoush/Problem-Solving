def searchRange(nums, target: int):
    if not nums : return [-1,-1]
    l=0
    h=len(nums)-1
    res=[]
    while l <= h:
        mid=(h+l)//2
        if nums[mid]==target:
            res.append(mid)
            l=mid+1
            h=mid-1
        elif nums[mid] > target:
            h=mid-1
        elif nums[mid] < target:
            l=mid+1
        else:
            res.append(mid)
    return res if res else [-1,-1]
nums = [2,2]
target = 2
print(searchRange(nums,target))
            