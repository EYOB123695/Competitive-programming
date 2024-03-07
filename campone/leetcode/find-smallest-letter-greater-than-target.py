class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left  = 0 
        right = len(letters) - 1 
        n = len(letters) -1 
        print(letters[-1])
        
       
        if target >= letters[n] or target < letters[0]: 
            return  letters[0] 

        while left <= right:                       
            mid = (left + right) // 2 
            if  target >= letters[mid] : 
                left = mid + 1  
               
              
            if target < letters[mid]:
                right = mid - 1 
                
           
        return letters[left]
        
            
            





        




        

        