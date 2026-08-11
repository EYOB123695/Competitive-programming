class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        val =  1
        sum = nums[0]
        final = nums[0]
        check = val
        for i in range(1,len(nums)):
            if nums[i-1] + 1 == nums[i] :
                val +=1 
                sum += nums[i] 
            else :
                break
                
              
     
                
     
        while sum in set(nums):
             sum +=1 
        return sum

            


        