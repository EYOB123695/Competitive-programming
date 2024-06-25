# Problem: Get Equal Substrings Within Budget - https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost = 0
        l = 0
        ans =  0
        for i in range(len(s)):
            cost +=  abs(ord(s[i]) - ord(t[i])) 
            while cost > maxCost:
                cost-= abs(ord(s[l]) - ord(t[l]))
                l +=1 
            ans = max(ans,i - l + 1)
        return ans

          
           

