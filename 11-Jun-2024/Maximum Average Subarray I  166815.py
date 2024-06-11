# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        average = 0
        sum = 0 
        maxaverage=float('-inf')
        ans = 0
        l = 0
        r = k

        prefixsum=[0] * (len(nums)+1)


        for i in range(len(nums)):
             
            prefixsum[i+1]  = prefixsum[i] + nums[i] 
        
        while r < len(prefixsum) :
        
            
            sum = prefixsum[r] - prefixsum[r-k]
             
            maxaverage =max(sum,maxaverage) 
            r+=1
            
        
        
        return maxaverage / k
       

        
