# Problem: Minimum Bit Flips to Convert Number - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        x = start ^ goal 
        print(x)
        print(bin(x)[2:])
        ans = 0
        for i in range(32):
            if (x & (1<<i)):
                ans +=1
            
        return ans 
        