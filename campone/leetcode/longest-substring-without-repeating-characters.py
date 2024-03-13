class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        r = 0
        seen = defaultdict(int)
        ans = 0
        def valid(dict):
            for i , value in dict.items():
                if value > 1 :
                    return False
            return True

        for r in range(len(s)):
            seen[s[r]]+=1
             
            
            while not valid(seen) and l < len(s):
                
                seen[s[l]]-=1
                l+=1
            
            
            ans = max(r-l+1,ans)   
           
                
                
            
        
            
        return ans


        