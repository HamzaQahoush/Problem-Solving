def productExceptSelf( nums) :
    
#         res=[0]*len(nums)
#         L= len(nums)
    
#         for i in range(L):
#             curr_product=1
#             for j in range(L):
#                 if j==i : continue 
#                 else:
#                     curr_product*=nums[j]
#             res[i]=curr_product
#         return res

    L=len(nums)
    res=[1]*L
    
    pre_product=1
    for i in range(L):
        res[i]*=pre_product
        pre_product*=nums[i]
    
    post_product=1
    
    for j in range(L-1,-1,-1):
        res[j]=res[j] *post_product
        post_product*=nums[j]
    return res
        
        
        
nums = [4,3,2,1,2]
# [1,2,6,24]
print (productExceptSelf  (nums))

          
            