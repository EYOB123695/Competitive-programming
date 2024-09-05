# Problem: Number of Smooth Descent Periods of a Stock - https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        dp = [1] * len(prices)
        for i in range(len(prices)-2,-1,-1):
            
                if prices[i] - 1 == prices[i+1]:
                    dp[i]= dp[i+1] + 1  
        val = sum(dp)
        return val
                    
        return dp[0] + len(prices) if dp[0] != 1 else len(prices) 
                




        