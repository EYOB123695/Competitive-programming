# Problem: Best Time to Buy and Sell Stock II - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(i,stock):
            if i >= len(prices):
                return 0
            if (i,stock) not in memo:
                if stock:
                    memo[(i,stock)] = max( dp(i+1,False)+ prices[i], dp(i+1,True)) 
                else:
                    memo[(i,stock)] = max( dp(i+1,False), dp(i+1,True)- prices[i]) 

            return memo[(i,stock)]
        return dp(0,False)