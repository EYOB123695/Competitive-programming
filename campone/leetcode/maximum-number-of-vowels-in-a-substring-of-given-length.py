class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0 
        r = 0 
        ans = 0
        se={"a","e","i","o","u"}
        
        count= 0
        for r in range(len(s)):
            if r-l +1 > k:
                if s[l] in se:
                    count-=1
                l+=1
            if s[r] in se:
                count+=1


               
                
            ans = max(ans,count)
              
                
                    
        return ans



            

