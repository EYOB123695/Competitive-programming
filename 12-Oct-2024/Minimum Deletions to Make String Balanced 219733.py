# Problem: Minimum Deletions to Make String Balanced - https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        arright = [0] * len(s)
        count = 0 
        for i in range(len(s)-1,-1,-1):

            if s[i] == "a":
                count +=1 
            arright[i] = count
      
        dp = [ 0] * len(s)
        counttwo = 0 
        for i in range(len(s)):
            if s[i] =="b":
                dp[i] = counttwo + arright[i]
                counttwo += 1 
            else:
                dp[i] = counttwo + arright[i] -1

            
      
        return min(dp)






        