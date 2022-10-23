from sortedcontainers import SortedList

def countSmaller(nums):
    # o(N)
    # count=[0]*len(nums)
    # for i,n in enumerate (nums):
    #     l=r=i
    #     while r <len(nums):
    #         if nums[l] > nums[r]:
    #             count[i]+=1
    #         r+=1
    # return count

    # olog(N)
    # rev -> [1,6,2,5]
    ans=[]
    sl=SortedList()
    for n in reversed(nums):
        idx=sl.bisect_left(n)
        ans.append(idx) 
        sl.add(n)
    return  ans[::-1]



print(countSmaller( [5,2,6,1]))