# Problem: Count Smaller Numbers After Self - https://leetcode.com/problems/count-of-smaller-numbers-after-self/

from sortedcontainers import SortedList 
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = []
        arr = SortedList(nums)
        

        for i in nums:
            idx = arr.bisect_left(i)
            ans.append(idx)
            del arr[idx]  
        return ans


        





