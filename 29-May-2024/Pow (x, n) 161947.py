# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recur(x,n):

            if x == 0:
                return 0
            elif n  == 0:
                return 1 
            c = recur(x,n//2)
            c = c * c
            if n % 2 != 0:
                return x * c
            else:
                return c

        ans = recur(x,abs(n))
        if n >=0:
            return ans 
        else :
            return 1 /ans 

        
             
            
                




            
            

     
        

            

         
        

        


        