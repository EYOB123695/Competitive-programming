# Problem: Binary Number with Alternating Bits - https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        curr = n & 1 
        next = ((n >> 1) & 1) 
        while n :
            if next == curr :
                return False 
            curr = n & 1 
            next = ((n >> 1) & 1)
            n>>= 1
        return True