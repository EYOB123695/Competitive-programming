# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        n = len(nums)
        for i in range(len(nums)):
            ans = (i + nums[i]) % n 
            result[i] = nums[ans ]
        return result


        