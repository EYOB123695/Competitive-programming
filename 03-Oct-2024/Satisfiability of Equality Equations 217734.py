# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent={i:i  for i in range(26)}
        def find(x):
            while parent[x] != x:
                x  = parent[x]  
            return x
           
        def union(x,y):
            parx = find(x)
            pary = find(y)
            if parx != pary:
                parent[parx] = pary 
        for i in equations:
            if i[1] == "=":
                parx = find(ord(i[0])- 97 )
                pary = find(ord(i[-1]) - 97  )
                if parx != pary: 
                 
                    union((ord(i[0])- 97),(ord(i[-1])- 97 )) 
                
        for i in equations:
            if i[1] == "!":
                parx = find(ord(i[0])- 97 )
                pary = find(ord(i[-1]) - 97  )
                if parx == pary:
                    return False 
        return True





        