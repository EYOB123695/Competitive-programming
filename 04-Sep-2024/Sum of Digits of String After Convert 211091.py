# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        x = []
        for  i in s:
            x.append(str((ord(i) - ord("a") + 1)) )
        
        val = sum(int(digit) for digit  in "".join(x)) 
        for _ in range(k - 1):
            val = sum(int(digit) for digit in str(val))
        return val



            
        




        