
import math



# Problem 1
"""
write a function that recieve an list and return
the second max number. 
[1,2,8,6,9,5] -- > 8 
"""


def getSecondMax(nums):

    max_no = max(nums)
    second_max = float("-inf")
    for n in nums:
        if n != max_no and n > second_max:
            second_max = n
    return second_max


# print('getSecondMax =>>',getSecondMax([1,2,8,6,9,5]))
#########################################


# Problem 2
"""
write a function that recieve an list and return
the index of First repeated number. 
[1,3,4,5,6,5,3,7,9] --> 1 for #3
"""


def get_index_of_first_repeated_no(nums):
    dic = {}
    index = 0
    for i, v in enumerate(nums):
        if v not in dic:
            dic[v] = i
        else:
            index = dic[v]
            break
    return index


print('get_index_of_first_repeated_no =>>',get_index_of_first_repeated_no([1,3,4,5,6,5,3,7,9]))

# Problem 3
##########################
"""
write a function that recieve an list and return
the SUM  of equal  numbers.
 sum_consecutive 
[2,2,2,7,3,3,1,2] => [6, 7, 6, 1, 2]
"""


def sum_consecutive(nums):
    curr = nums[0]  # 2 / 2 / 7 / 3 /3
    result = [nums[0]]  # [6,7] /
    for n in nums[1:]:  # 2 / 2 /7/3
        if curr == n:  # 2=2 /2=2/
            result[-1] += n  # 4 /6
            curr = n  # 2 / 2
        else:
            result.append(n)
            curr = n
    return result


# print("sum_consecutive----",sum_consecutive([2,2,2,7,3,3,1,2]))


# Problem 4
##########################
"""
write a function that recieve an list and return
the reverse of its values.
 sum_consecutive 
 [5, 7, 3, 1, 2] ===> [2 ,1 ,3 ,7 ,5]
"""


def array_reverse(lst):
    # solution 1
    # result=[]
    # while lst:
    #     result.append(lst.pop())
    # return result

    result = []
    for i in range(len(lst) - 1, -1, -1):
        result.append(lst[i])
    return result


# print('array_reverse---->',array_reverse([5, 7, 3, 1, 2]))


# Problem 5
##########################
"""
write a function that recieve an a number and return
the reverse of its value.
 sum_consecutive 
 123===> 321
"""


def reverse_no(no):
    b = 0
    while no > 0:  # 123 / 12 / 1
        b = b * 10 + no % 10  # 3 / 32 / 320+1 / 321
        no = no // 10  # 12 / 1  / 0-
    return b


# print('reverse_no ------>', reverse_no(123))

# Problem 6 / next greater element
######################################################################################
question = "https://leetcode.com/problems/next-greater-element-i/"
"""
 nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]


"""


def nextGreaterElement(nums1, nums2):
    num1Idex = {n: i for i, n in enumerate(nums1)}
    print(num1Idex)
    res = [-1] * len(nums1)
    for i, v1 in enumerate(nums2):
        if v1 not in num1Idex:
            continue
        for j, v2 in enumerate(nums2[i + 1 :]):
            if v2 > v1:
                idx = num1Idex[v1]
                res[idx] = v2
                break
    return res


# print("nextGreaterElement", nextGreaterElement([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7]))

# Problem 7
######################################################################################
"""
write a function that recieve an a number and return
sum of each number.
 123===> 6
"""


def sum_of_each_no(a):
    sum_no = 0  # 0/3

    while a > 0:
        b = a % 10  # 3
        sum_no += b  # 3
        a = a // 10  # 12
    return sum_no


# print(sum_of_each_no(123))

# Problem 8
######################################################################################
"""
write a function that recieve an a number and return
if is it prime on not
"""


def is_prime(n):
    boundary = int(math.sqrt(n)) + 1
    for i in range(2, boundary):
        if n % i == 0:
            return n, False
    if n >= 2:
        return n, True


# print("is_prime", is_prime(9))

# Problem 9 -- Product of Array Except Self
######################################################################################
"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

https://leetcode.com/problems/product-of-array-except-self/
Input: nums = [1,2,3,4]
[1,1,2,6,12]
[]
Output: [24,12,8,6]

"""


def productExceptSelf(nums):
    # o(n)2
    # result = [-1] * len(nums)
    # stack = nums[0]
    # for i, v in enumerate(nums):
    #     product = 1
    #     for k in nums[i + 1 :]:
    #         product *= k
    #     if stack != v or v == 0:
    #         result[i] = product * stack
    #         stack *= v
    #     else:
    #         result[i] = product

    # return result
    res = [1] * len(nums)
    prefix = 1
    for i, n in enumerate(nums):  # 0,1 /
        res[i] *= prefix  #
        prefix *= n
    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]
    return res


# Input: nums = [1,2,3,4]
# res =[1,1,2,6]
# []
# Output: [24,12,8,6]
# print(productExceptSelf([2, 5, 4, 3]))


# Problem 10 -. Longest Substring Without Repeating Characters

"""
Given a string s, find the length of the longest substring without repeating characters.

https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""


def lengthOfLongestSubstring(s: str) -> int:

    l = 0
    r = 0
    max_so_far = 0
    hashset = set()
    while r < len(s):
        if s[r] not in hashset:
            hashset.add(s[r])
            r += 1
            max_so_far = max(max_so_far, len(hashset))
        else:
            hashset.remove(s[l])
            l += 1

    return max_so_far


# print(lengthOfLongestSubstring("abcdbcbb"))


def longestPalindrome(s: str) -> str:
    if len(s) <= 1:
        return s
    start, end = 0, 0
    for i, chara in enumerate(s):
        odd = expand_from_mid(s, i, i)
        even = expand_from_mid(s, i, i + 1)
        len_ = max(odd, even)
        if len_ > (end - start):
            start = i - ((len_ - 1) // 2)
            end = i + (len_ // 2)
    return s[start : end + 1]


def expand_from_mid(s, left, right):
    if not s or left > right:
        return 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1


print("longestPalindrome", longestPalindrome("babad"))


def maxArea(height) -> int:

    max_area = 0
    for left, n in enumerate(height):
        for right, k in enumerate(height[left + 1 :], start=left + 1):
            width = right - left
            max_area = max(max_area, (min(height[left], height[right]) * width))
    return max_area


# [4,3,2,1,4] [1, 8, 6, 2, 5, 4, 8, 3, 7]
height = [4, 3, 2, 1, 4]

# print("maxArea", maxArea(height))

import itertools


def threeSum(nums):
    s = set()
    for i, n in enumerate(nums):
        curr_Sum = 0

        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                curr_Sum = nums[j] + nums[k] + n
                if curr_Sum == 0:
                    s.add((n, nums[j], nums[k]))

    res = [sorted(list(ele)) for (ele) in s]
    unique_result = []
    for r in res:
        if r not in unique_result:
            unique_result.append(r)
    return unique_result


# nums = [-1, 0, 1, 2, -1, -4]
# nums = [3, -2, 1, 0]
nums = [-1, 0, 1, 0]

# nums = [-2, 0, 1, 1, 2]
print("threeSum", threeSum(nums))


def get_numbers_count(nums, x):
    dic = {}
    for n in nums:
        dic[n] = nums.count(n)

    return dic.get(x)


# print(get_numbers_count(nums, n=None))


# SingleTone pattern
class OnlyOne:

    _singletone = None

    def __new__(self):
        if not self._singletone:
            self._singletone = super(OnlyOne, self).__new__(self)
        return self._singletone


o1 = OnlyOne()
o2 = OnlyOne()
# print(o1 == o2)


def isValid(s: str) -> bool:

    dic = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for i, v in enumerate(s):
        if v == "(" or v == "[" or v == "{":
            stack.append(v)
        elif v == ")" or v == "]" or v == "}":
            last = stack[-1]
            if dic[last] == v:
                stack.pop()
    return True if not stack else False


# print("isValid", isValid("()"))


def find_averages_of_subarrays(K, arr):
    end = len(arr) - K + 1
    res = []
    for i, n in enumerate(arr[0:end]):
        sum_ = 0
        for j in arr[i : i + K]:
            sum_ += j
        res.append(sum_ / K)
    return res


def peakIndexInMountainArray(arr) -> int:

    l, r = 0, len(arr) - 1

    while l < r:
        mid = (l + r) // 2
        if arr[mid] >= arr[mid + 1]:
            r = mid
        else:
            l = mid + 1
    return l


def main():
    # result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    # print("Averages of subarrays of size K: " + str(result))
    print("peakIndexInMountainArray", peakIndexInMountainArray([0, 1, 0]))


main()


def maximumUnits(boxTypes, truckSize: int) -> int:
    boxTypes.sort(key=lambda arr: -arr[1])

    total_unit = 0
    for no_box, u in boxTypes:
        if truckSize <= no_box:
            total_unit += truckSize * u
            break
        total_unit += no_box * u
        truckSize -= no_box

    return total_unit


print(maximumUnits([[1, 3], [2, 2], [3, 1]], 4))


def longestConsecutive(nums) -> int:

    nums_set = set(nums)
    longest = 0
    for n in nums:
        if (n - 1) not in nums_set:
            length = 0
            while (n + length) in nums_set:
                length += 1
                longest = max(length, longest)
    return longest


nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))


def fib(n: int) -> int:
    # f=[0,1]

    # for i in range(2,n+1):
    #     f.append(f[i-1]+f[i-2])
    # print(f)
    # return f[n]
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b


print(fib(3))


def isInterleave(s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False
    dp = {}

    def dfs(i, j):
        if i == len(s1) and j == len(s2):
            return True
        if (i, j) in dp:
            return dp[(i, j)]
        if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
            return True
        if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
            return True
        dp[(i, j)] = False
        return False

    print(dp)
    return dfs(0, 0)


print("isInterleave", isInterleave("aabcc", "dbbca", "aadbbcbcac"))


def minCostClimbingStairs(cost) -> int:
    step1 = 0
    step2 = 0

    for i in range(len(cost) - 1, -1, -1):
        curr_step = cost[i] + min(step1, step2)
        step1 = step2
        step2 = curr_step
    return min(step1, step2)


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# cost=[10,15,20]
# print(minCostClimbingStairs(cost))


def gridTraveler(m, n, cache={}):
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    if (m, n) in cache:
        return cache[(m, n)]

    cache[(m, n)] = gridTraveler(m - 1, n, cache) + gridTraveler(m, n - 1, cache)
    return cache[(m, n)]


#print("gridTraveler==>", gridTraveler(18, 18))


def makesquare( matchsticks) -> bool:
    each_side=  sum(matchsticks)//4
    if each_side!=sum(matchsticks)/4:
        return False
    sides=[0]*4
    matchsticks.sort(reverse=True)

    def back_track(i):
        if i == len(matchsticks):
            return True
        for j in range(4):
            if sides[j]+matchsticks[i] <=each_side:
                sides[j]+=matchsticks[i]
                if back_track(i+1):
                    return True
                sides[j]-=matchsticks[i]
        return False     
        
    return back_track(0)

matchsticks = [1,1,2,2,2]
print ('makesquare', makesquare(matchsticks))

def find_all_duplicate(nums):
    res=[]
    for i,v in enumerate(nums):
        idx=abs(nums[i])-1
        if nums[idx]<0 :
            res.append(idx+1)
        else:
            nums[idx]=-nums[idx]
    return res
nums = [4,3,2,7,8,2,3,1]
print('find_all_duplicate',find_all_duplicate(nums))

            

def findDuplicate( nums) -> int:
    # sol1
#         res=set()
#         for n in nums : 
#             if n not in res:
#                 res.add(n)
#             else: return n
    # solution 2

    # slow,fast=0,0
    # while True:
    #     n=slow
    #     slow=nums[slow]
    #     fast=nums[nums[fast]]
    #     if slow == fast:
    #         break
    # slow2=0
    # while True:
    #     slow=nums[slow]
    #     slow2=nums[slow2]
    #     if slow2==slow:
    #         return slow
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if i == j:  # next index if the index and value match
            i += 1
        else:
            if nums[i] != nums[j]:  # swap
                nums[i], nums[j] = nums[j], nums[i]
            else:  # this is the duplicate
                return nums[i]
nums = [1,3,4,2,2]
print('findDuplicate',findDuplicate(nums))   

def missingNumber( nums) -> int:
    i=0
    while i < len(nums):
        j=nums[i] # j=2
        if nums[i]<len(nums) and nums[i] != nums[j] :
            nums[i],nums[j]=nums[j],nums[i]
        else: 
            i+=1
    for idx in range(len(nums)):
        if nums[idx] !=idx :
            return idx
    return len(nums)
nums=[3,0,2]

print('missingNumber',missingNumber(nums))



"""
minSum
Input:
N = 6
arr[] = {6, 8, 4, 5, 2, 3}
Output:
604
Explanation:
The minimum sum is formed by numbers 
358 and 246
"""
def minSum(arr, n):
    
    arr.sort()
    print('arr',arr)
    num1=num2=0
    for i in range(len(arr)):
        if i%2 ==0 and i < n :
            num1=num1*10 + arr[i]

        else:
            num2=num2*10 + arr[i]
    
    return num1+num2

arr=[6, 8, 4, 5, 2, 3]
n=5
print('minSum', minSum(arr,n))


def maxAreaOfIsland( grid) -> int:

    rows=len(grid)
    col= len(grid[0])
    seen=set()
    def dfs(r,c):
        if (r <0 or r==rows or c <0 or c==col or (r,c) in seen or grid[r][c]==0 ): return 0
        
        seen.add((r,c))
        
        return (1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1))

    max_area=0
    for r in range(rows):
        for c in range(col):
            max_area=max(max_area,dfs(r,c))
    return max_area
grid=[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print('maxAreaOfIsland',maxAreaOfIsland(grid))



def romanToInt( s: str) -> int:
    dic = {'I' : 1 , 'V':5 ,'X':10,'L':50,'C':100,'D':500,'M':1000}
    stack=[]
    res=0
    for c in s:     
        v=dic.get(c,-1)
        if stack : 
            if c == "M" and stack[-1] == 'C' or  c == 'C' and stack[-1] == 'X' or c=='V' and stack[-1]=='I':
             v=dic.get(c)-(2*dic.get(stack[-1]))
            

        res+=v
        stack.append(c)
    return res

print ('romanToInt' , romanToInt("MCMXCIV"))


def canSum(targetSum, numbers):
    def helper(targetSum,numbers,memo):
        if targetSum in memo :
            return memo[targetSum]
        
        if targetSum == 0:
            return True
        if targetSum < 0:
            return False

        for n in numbers:
            remainder = targetSum - n
            if helper(remainder, numbers,memo)==True:
                memo[targetSum]=True
                return True

        memo[targetSum]=False
        return False
    return helper(targetSum,numbers,memo={})


print(canSum(7, [2, 3])) # True
print(canSum(7, [5, 3, 4, 7])) # True
print(canSum(7, [2, 4])) # False
print(canSum(8, [2, 3,5])) # True

print(canSum(300, [7,14]) ,'Taffffffffffff') # False





    
def subarraySum( nums, k: int) -> int:
    ans , prefsum, d = 0,  0, {0:1}
    for num in nums:
        prefsum += num
        if  prefsum-k  in  d:
            ans = ans + d[prefsum-k]
        d[prefsum] = d.get(prefsum, 0) + 1
    return ans
            
nums=[1,1,1]
k=2
print('subarraySum',subarraySum(nums,k))


"""
https://leetcode.com/problems/pascals-triangle/
"""
def pascal_triangel(numRows):

    res=[[1]]
    for _ in range(1,numRows):
        temp=[0]+res[-1]+[0]
        row=[]
        for i in  range(len(res[-1])+1):
            row.append(temp[i]+temp[i+1])
        res.append(row)
    return res
print('pascal_triangel',pascal_triangel(5))



def numMatchingSubseq( s: str, words) -> int:
    count=0
    for word in words:
        if isSubsequence(s,word)==True:
            count+=1
    return count
    
    
def isSubsequence(s: str, t: str) -> bool:
    i=j=0
    flag=False
    while i < len(s) and j < len(t):
        if s[i]!=t[j]:
            flag=False
        if s[i]==t[j]:
            i+=1
            flag=True
        
        j+=1
    return flag
            

s = "abcde"
words = ["a","bb","acd","ace"]

print('numMatchingSubseq',numMatchingSubseq(s,words))



"""
min = 1;
max = 5;
//output
//[2,3,4]
"""

def range_between_min_max(mx,mn):
    res=[]
    re=[2,3,4]
    for i in range(mn+1,mx):
        res.append(i)
    if res==re:print(True)
    return res
print('range_between_min_max',range_between_min_max(5,1))
