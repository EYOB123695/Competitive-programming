# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
       
        minval = arrays[0][0]
        maxval = arrays[0][-1]
        ans = -float("inf")

        for i in range(1,len(arrays)):
            ans = max( ans,maxval - arrays[i][0], arrays[i][-1]- minval)
            maxval = max(maxval,arrays[i][-1])
            minval = min(minval,arrays[i][0])
        return ans 

            
