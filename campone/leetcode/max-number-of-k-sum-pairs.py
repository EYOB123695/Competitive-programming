class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l = 0
        r = len(nums)-1
        count = 0 
        nums.sort()
        while l < r : 
            
            if nums[r] + nums[l] == k:
                count +=1 
                l+=1
                r-=1
            elif nums[r] + nums[l] < k:
                l+=1
            else:
                r-=1 
        return count
        
        




        