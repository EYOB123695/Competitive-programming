# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        ans= 0
        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        for j in range(len(nums)-1 ,-1,-1):
            while stack and nums[j] >= nums[stack[-1]]:
                val = stack.pop()
                ans = max(ans,j -val )


        return ans

