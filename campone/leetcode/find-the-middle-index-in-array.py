class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefixsum = [0] * len(nums)
        prefixsum[0] = nums[0] 
        for i in range(1,len(nums)):
             
            prefixsum[i]  += prefixsum[i-1] + nums[i]  
        print(prefixsum)
        for j in range(len(nums)):
            if j == 0 :
                left = 0
            else:
                left = prefixsum[j-1]
            right = prefixsum[-1] - prefixsum[j] 
            
            if left == right : 
                return  j
        return -1





        
        