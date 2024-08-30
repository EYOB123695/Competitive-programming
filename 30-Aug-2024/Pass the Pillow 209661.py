# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        t = 1 
        i = 1
        while time :
            i +=t
            if i == n or i == 1:
                t= t*-1
            time-=1
        return i
        l = 1
        val = 1
         

        # while time :
        #     l += val
        #     if l == n or l == 0:
        #         val = val * -1
        #     time-=1
            
            
        # return l

            



