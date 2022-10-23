
# [1,2,4,6,5,8,9]
# (1,9) (2,8) (4,6)
def count_pairs(nums,target):
    dic={}
    for n in nums:
        diff=target-n
        if n not in dic and diff != n:
            dic[diff]=n
    return len(dic.keys())


print(count_pairs([1,2,4,6,5,8,9],10))