class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        result = float("inf")
        for i in range(len(nums)):
            if nums[i] == target:
                result = min(result,abs(i-start))
        return result


        