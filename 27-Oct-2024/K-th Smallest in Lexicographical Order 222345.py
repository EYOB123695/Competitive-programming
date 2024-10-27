# Problem: K-th Smallest in Lexicographical Order - https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        cur =  1 
        i = 1 
        def help(curr):
            res = 0 
            nei = curr  + 1 
            while curr <= n:
                res += min(nei, n +1 ) - curr
                curr *= 10 
                nei *= 10 


            return res


        while i < k :
            step = help(cur)
            if step + i <= k :
                cur +=  1 
                i += step 
            else :
                cur *= 10 
                i += 1  
        return cur




        
        
        
                

        
       

            
            

        