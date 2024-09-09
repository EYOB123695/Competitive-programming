# Problem: Find Missing Observations - https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        ans = []
        sumone = sum(rolls)
      
        sumtwo = mean * (n + len(rolls)) - sumone 
        remain = sumtwo 
        
        if n <= sumtwo <= 6 * n:
            ans = [1] * n 
            i = 0 
            v = sum(ans)
            remain  = remain - v
          
            for i in range(len(ans)):
                diff  = min(5, remain) 
                
                ans[i] += diff 
                remain -= diff
               
                  

        return ans 
        