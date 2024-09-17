# Problem: Maximize Score of Numbers in Ranges - https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        def check(mid):
            curr = start[0]
            for i in range(1,len(start)):
                curr += mid
                if curr  > start[i] + d:
                    return False 
                curr = max(curr,start[i])
            return True 
        l =  0 
        start.sort()
        n  = len(start)
        r = ((start[-1] +  d *(n -1)) - start[0])
        ans = 0
        while l <= r:
            mid = l + (r - l)// 2 
            if check(mid):
                ans = mid
                l = mid +1 
            else:
                r = mid - 1 
        return ans

 



        