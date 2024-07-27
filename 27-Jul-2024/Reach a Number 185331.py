# Problem: Reach a Number - https://leetcode.com/problems/reach-a-number/

class Solution:
    def reachNumber(self, target: int) -> int:
        ans = 0 
        step = 0
        target = abs(target)
        while ans < target or (ans -target) % 2 != 0:
            step+=1
            ans += step
           
        return step


        




        