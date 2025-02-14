# Problem: 3Sum Closest  - https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        answer = float("inf")
        for i in range(len(nums) -2) : 
            left , right = i +  1 , len(nums  ) - 1 
            while left < right:
                curr = nums[i] + nums[left] + nums[right]
                if abs(target - curr) < abs(target - answer):
                    answer = curr 
                if curr < target: 
                    left += 1 
                elif curr > target : 
                    right -= 1 
                else :
                    return curr 
        return answer