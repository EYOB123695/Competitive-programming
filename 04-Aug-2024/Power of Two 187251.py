# Problem: Power of Two - https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n >= 2:
            n/=2
        if n == 1:
            return True 
        else:
            return False
        