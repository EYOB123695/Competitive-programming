# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        curr =1 
        for i in range(1,n+1):
          if i == curr * 2 :
            curr  *= 2
          dp[i]  = 1 + dp[i-curr]  
        return dp
        
          





        