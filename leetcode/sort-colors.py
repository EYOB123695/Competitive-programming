class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        low = 0  
        high = len(nums) - 1 
        i = 0  

        while i <= high:
            if nums[i] == 0:
                
                nums[low], nums[i] = nums[i], nums[low]

            
                low += 1
                i += 1
            elif nums[i] == 2:
                
                nums[i], nums[high] = nums[high], nums[i]

                
                high -= 1
            else:
                
                i += 1
        

            

        


            


                 


        