# Problem: K Items With the Maximum Sum - https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans = 0
        while k > 0 and numOnes > 0:
            ans += 1
            numOnes -= 1
            k-=1
        while k > 0 and numZeros> 0:
            k-=1
            numZeros -= 1
        while k > 0 and numNegOnes > 0:
            k-=1
            ans -= 1
            numNegOnes -= 1
        return ans

            


        
        
        








        