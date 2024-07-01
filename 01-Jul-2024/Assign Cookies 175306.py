# Problem: Assign Cookies - https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        content=0
        r=0
        l=0
        
        g.sort()
        s.sort()
        while r < len(g) and l < len(s):
            if  s[l] >= g[r] :
                content+=1
                r+=1
            
            l+=1
        return content 



