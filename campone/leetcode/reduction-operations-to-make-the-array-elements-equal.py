class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        operations = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1] :
                operations+=1 
            count+=operations
        return count

        