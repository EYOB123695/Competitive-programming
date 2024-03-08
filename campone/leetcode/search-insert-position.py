class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target :
                return i
        l = 0 
        r= len(nums)-1
        print(len(nums))
        while l <= r:
            mid = (l + r) // 2  
            if nums[mid] > target:
                r = mid - 1  
            else :
                l = mid +1 
        return l






        