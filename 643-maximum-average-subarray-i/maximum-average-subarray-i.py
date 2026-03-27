class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
         maxval = -inf
         windowSum = (sum(nums[:k]))
         maxval = max(maxval, windowSum)
         left = 0

         for num in nums[k:]:

            windowSum -= nums[left]

            windowSum += num
            maxval = max(maxval, windowSum)
            left +=1

    

         return maxval/k 






            





        