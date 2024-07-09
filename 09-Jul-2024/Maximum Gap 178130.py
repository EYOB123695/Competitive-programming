# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        if len(nums) < 2:
            return  0

        for i in range(len(nums)-1):
            ans = max(ans,nums[i+1]- nums[i])
        return ans

        