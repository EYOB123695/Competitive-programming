# Problem: Find Peak Element - https://leetcode.com/problems/find-peak-element

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
    
        l = 0
        r = len(nums) -1
        if len(nums) == 1 :
            return 0
        while l < r :
            mid = l +(r -l) // 2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid -1 ]:
                return mid 
            elif nums[mid] < nums[mid+1]:
                l = mid +1 
            else:
                r = mid -1 
        return l
         

