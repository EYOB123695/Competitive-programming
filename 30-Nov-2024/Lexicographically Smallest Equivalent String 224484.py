# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)
        parent = {chr(i):chr(i) for i in range(97,123)}
        ans = []
        def find(x):
            while x != parent[x]:
                parent[x]= parent[parent[x]]
                x = parent[x]
            return x
        def union(x,y):
            parx = find(x)
            pary = find(y)
            if parx != pary:
                if parx < pary:
                    parent[pary] = parx 
                else :
                    parent[parx] = pary
        for i in range(n):
            union(s1[i],s2[i])
        
        for i in range(len(baseStr)):
            x= find(baseStr[i])
            ans.append(x)
        return "".join(ans)
        