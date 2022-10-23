def reverse_no(num):
    reversed_num=0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num
num=1234
print('reverse_no',reverse_no(num))


def make_increasing(nums):
    res=False
    test_list=[]
    test_list.extend(nums)
    test_list.sort()

    if test_list == nums: 
        return True


    for i,v in enumerate(nums[1:], start=1):
        if v < nums[i-1]:
            rev=reverse_no(nums[i-1])
            if nums[i-2]<rev < v :
                nums[i-1]=rev
                res=True
    return res





nums=[1, 5, 10, 20]
# True

print (make_increasing(nums))


