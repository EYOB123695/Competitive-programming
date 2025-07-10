# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = sum(nums[:k])
       
        sumtwo = curr
        j = 0 
        for i in range(k, len(nums)):
            curr += nums[i]
            curr -= nums[j] 
            j+=1 
            sumtwo = max(sumtwo,curr) 
            
        
        return (sumtwo / k) 




           
            

            
            







        