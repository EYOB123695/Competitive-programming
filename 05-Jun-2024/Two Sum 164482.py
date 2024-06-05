# Problem: Two Sum - https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for  idx,val in enumerate(nums):
            diff = target - val
            if diff in dict:
                return [dict[diff],idx]
            
            dict[val] = idx
