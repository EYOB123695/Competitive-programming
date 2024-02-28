class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count=0
        nums.sort()
        i = 0
        r = len(nums)-1
        while i < r:
            if nums[i] + nums[r] < target:
                d = r-i
                count+=d 
                i+=1
                
            else :
                r-=1
        return count