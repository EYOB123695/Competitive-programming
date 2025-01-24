# Problem: Non-decreasing Array - https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0 
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                count += 1
            if 1 < i < len(nums)-1 and nums[i-2] > nums[i] and nums[i+1] < nums[i- 1 ]:
                return False
        return False if count >= 2 else True
            
        