# Problem: Longest Subarray With Maximum Bitwise AND - https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        val = max(nums)
        count = 0 
        res = 0
        for i  in nums:
            if i == val:
                count+= 1 
            else:
                count = 0 
            res = max(res,count)
        return res

        