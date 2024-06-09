# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=  True)
        for i in range(len(nums)-2):
            x=nums[i]
            y=nums[i+1]  
            z=nums[i+2]
            if x < y+z : 
                return x+y+z
        
        return 0

        