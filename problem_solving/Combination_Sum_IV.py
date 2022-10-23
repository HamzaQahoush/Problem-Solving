def combination_sum(nums,target):
    dp={0:1}

    for  total in range(1,target+1):
        dp[total]=0
        for n in nums:
            dp[total]+=dp.get(total-n,0)
    return dp[target]
        # dp
        # dp = [0] * (target+1)   # target+1 because we need dp[0]
        # dp[0] = 1
        
        # for t in range(1, target+1):
        #     for num in nums:
        #         if t>=num:
        #             dp[t] += dp[t-num]
                    
        # return dp[target]
nums = [1,2,3]
target = 4

print(combination_sum(nums,target))