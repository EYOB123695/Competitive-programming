# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      
       profit = 0
       if len(prices) == 1:
            return 0

       minval = prices[0]
       for i in range(1,len(prices)):
          
           profit = max(profit,prices[i] - minval)
           minval = min(prices[i],minval)

       
       return profit
           











       
       

        
        




           



        