class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        left , right = -1 , len(nums)
        flag = False                    

        while left+1 < right :
            mid = (left+right)//2  
            if nums[mid]== target:
                flag= True

            if nums[mid] >=  target :
                right = mid  
               
            else:
                left = mid  
               
        firstposition = right  
        left , right = -1 , len(nums)
        
        while left+1 < right :
            mid = (left+right)//2  

            if nums[mid] <=  target : 
                left = mid                      
            else:
                right = mid 
        lastposition = left
        
        

        if not flag:
            return [-1,-1]
        else :
            ans.append(firstposition)
            ans.append(lastposition)
            return ans

       

            
                       




                

        

        