# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        ans = 0
        for i  in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2 
                nums[i+1] = 0 
        l = 0
        r = 0
        while r < len(nums):
            if nums[r] != 0:
                nums[l] , nums[r] = nums[r] , nums[l]
                l+=1 
            r+=1 
        return nums

        