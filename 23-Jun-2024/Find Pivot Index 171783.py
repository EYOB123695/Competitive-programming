# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        prefixsum = [0] *(len(nums)+1)
        prefixsumback = [0] * (len(nums) + 1)

        for  i in range(len(nums)):
            prefixsum[i+1] = nums[i] + prefixsum[i]
        for  i in range(len(nums)-1,-1,-1):
            prefixsumback[i] = nums[i] + prefixsumback[i+1]
        for i in range(len(prefixsum)-1):
            if prefixsum[i] == prefixsumback[i+1]:
                return i 
        
        return -1
