# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return  0
        nums_set = set(nums)
        length = 0 
        for i in range(len(nums)):
            if nums[i] - 1 not in nums_set:
                curr = nums[i]
                streak = 1
                while curr + 1 in nums_set:
                    curr = curr +1 
                    streak +=1 
                length = max(length , streak)
        return length


            






        