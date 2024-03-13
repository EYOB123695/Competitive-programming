class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        
        ans = []
        
        dicttwo = Counter(p) 
        l = 0 
        r  = k
        

        dic = Counter(s[:k])
        while r  < len(s):
           
            
            if dic == dicttwo:
                ans.append(l)
            dic[s[l]] -= 1
            l+=1 
            

           
            
            dic[s[r]] += 1 
            r+=1 
        if dic == dicttwo:
            ans.append(l)
        
        return ans   
           
            
            

            





