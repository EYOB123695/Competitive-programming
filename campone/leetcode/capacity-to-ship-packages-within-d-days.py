class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int: 
        def testfunction(mid):
            currday = 1
            capacity = mid 
            for w in weights:
                if capacity - w >= 0 :
                    capacity -= w 
                else:
                    currday += 1  
                    capacity =  mid - w               
                
                
                
                 
            if currday <= days:
                return True 
            else :
                return False
                
        
        r = sum(weights)
        l = max(weights)  
        
        while l <= r :
            mid = (l + r)//2 
            if testfunction(mid) :
                
                r = mid - 1   
            else : 
                l = mid + 1 
        return l
        





        
        
            
             
        




        

        



        

        