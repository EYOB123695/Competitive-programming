class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        dict = defaultdict(int)
        length = 0 
        l = 0
        for i in range(len(s)):
            dict[s[i]] +=  1 
            while dict[s[i]] > 2 :
                dict[s[l]] -= 1
                l+= 1  
            length  = max(length,i-l + 1 )
        return length

        