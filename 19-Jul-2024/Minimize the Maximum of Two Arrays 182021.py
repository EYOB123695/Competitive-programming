# Problem: Minimize the Maximum of Two Arrays - https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        def gcd(a,b):
            if b == 0:
                return a 
            return gcd(b,a% b)
        lcm = divisor1 * divisor2 // gcd (divisor1, divisor2)
        l = 1
        r = 2*(10**9)
       
        while l < r:
            mid = (l+r) // 2
            num1 = mid -(mid // divisor1)
            num2 = mid -(mid // divisor2 )
            num3 = mid -(mid // lcm)
            if num1 <  uniqueCnt1 or num2 <  uniqueCnt2 or num3 <( uniqueCnt1+ uniqueCnt2):
                l = mid +1
            else:
                
                r = mid 
        return l



            