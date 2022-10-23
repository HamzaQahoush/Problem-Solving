

def avoide_obstacles(nums):
    for i in range(2,max(nums)+2):
        flag=True
        for n in nums:
            if n % i == 0 :
                flag=False
                break
        if flag :
            return i
        
nums=[5, 3, 6, 7, 9]
print (avoide_obstacles(nums))
            