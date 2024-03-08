class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int: 
        l = 0
        r = 0 
        ans = 0
        countzero = 0
        while r < len(nums) :
            if nums[r] == 0:
                countzero +=1
                

            while countzero > k:
                if nums[l] == 0:
                    countzero-=1
                l +=1 

                
            
                
            ans = max (ans , r  - l + 1) 
                
            r +=1 
        return ans




                  

        


        