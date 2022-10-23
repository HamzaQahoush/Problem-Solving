#1365. How Many Numbers Are Smaller Than the Current Number
"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

example :
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
"""



def get_num_smaller(nums):
    # 1,2,2,3,8
    # solution 1

    dict_nums = {}
    # for i, number in enumerate(sorted(nums)):
    #     if number not in dict_nums:
    #         dict_nums[number] = i

    # numbers_less_than = []
    # for n in nums:
    #     numbers_less_than.append(dict_nums[n])

    # return numbers_less_than

    # solution 2 
    res=[0]*len(nums)
        
    for i,n in enumerate (nums):
        r=0         
        while r < len(nums):
            if n > nums[r]:
                res[i]+=1
            r+=1
    return res


print(get_num_smaller([8,1,2,2,3]))