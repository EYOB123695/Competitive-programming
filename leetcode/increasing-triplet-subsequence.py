class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        one = float("inf")
        two = float("inf")
        for n in nums:
            if n <= one:
                one=n
            elif n <= two :
                two=n
            else :
                return True
        return False
        
        

        
    
         


        