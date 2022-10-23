"""
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

def maxProfit( prices) -> int:
    mn=prices[0]
    curr=prices[0] # curr= 7 / 1 / 5 /3
    diff=0 # 0 / 4 / 4 / 5
    for p in prices[1:]: # p= 1 / 5 / 3 / 6
        mn=min(mn,p) # mn = 1 / 1 / 1 /1 
        diff=max(diff,p-mn) #diff= 0 / 4  / 4 / 5
        curr=p  # 1 / 5 / 3 / 6
    return diff

print (maxProfit(prices = [7,1,5,3,6,4]))