class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=1
        for h in range(l,len(nums)):
            if nums[h]!= nums[h-1]:
                nums[l]=nums[h]
                l+=1
        return l  
        


        