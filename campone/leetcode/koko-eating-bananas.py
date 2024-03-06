class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(mid): 
            k = mid
            hours = 0 
            for  p in piles:
                x=p / k 
                
                
                y=ceil(x) 
                
                hours+=y
                
                        
            if hours <= h :
                return True 
            else : 
                return False
                



        l = 1
        r = max(piles)
        while l <= r:
            mid = (l + r)// 2 
            
            if check(mid): 
                r = mid -1 
            else :
                l = mid + 1
        return l



        
        