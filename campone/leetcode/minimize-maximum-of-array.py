class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = nums[0]
        sum = nums[0]
        
        for i in range(1,len(nums)):
            sum+=nums[i]
            average = math.ceil(sum / (i+1)) 
            res = max(res,average) 
        return res

