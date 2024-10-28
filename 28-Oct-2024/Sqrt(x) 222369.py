# Problem: Sqrt(x) - https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return x
        
        l,h=1,x
        while l<=h:
            mid=(l+h)//2
            
            if mid*mid==x:
                return mid
            elif mid * mid > x:
                h = mid -1
            else:
                l= mid+1
        return h

        