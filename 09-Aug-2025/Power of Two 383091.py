# Problem: Power of Two - https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1 :
            return True 
        while n >= 2 :
            n = n / 2 
        if n == 1 :
            return True
        else:
            return False