# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(i,stock,sell):

            if i >= len(prices) or sell >= 2:
                return 0
            
           
            if (i,stock,sell) not in memo:
                if stock:
                    memo[(i,stock,sell)] = max( dp(i+1,False,sell+1)+ prices[i] , dp(i+1,True,sell)) 
                else:
                    memo[(i,stock,sell)] = max( dp(i+1,False,sell), dp(i+1,True,sell) - prices[i]) 

            return memo[(i,stock,sell)]
        return dp(0,False,0)

        