class Solution:
    def maxScore(self, s: str) -> int:
        
        dict = Counter(s)
        ans = 0
        left = 0
        right =dict["1"]
        
        prefixsum=[0] * (len(s)+1)


        for i in range(1,len(s)+1):
             
            prefixsum[i]  = prefixsum[i-1] +int(s[i-1]) 
       

        
        for i in range(1,len(prefixsum)-1):
            if prefixsum[i] == prefixsum[i-1]:
                left += 1
                
                sum = left + right 
                ans = max(sum,ans)
                

            elif prefixsum[i] > prefixsum[i-1]:
                right -= 1
                
                sum = left + right 
                ans = max(sum,ans)  

             
        
        return ans
            
              
        
        
        