# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        parent = {i:i for i in range(n)}
        rank = [1] * n 

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            parx = find(x)
            pary = find(y)
            if parx != pary:
                if rank[parx] > rank[pary]:
                    parent[pary] = parx
                elif  rank[pary] > rank[parx]:
                    parent[parx] = pary 
                else:
                    parent[parx] = pary
                    rank[pary] += 1
        
        for i in range(len(strs)-1):
            x = strs[i]

            for j in range(i+1,len(strs)):
                count = 0
                y = strs[j]
                for z in range(len(x)):
                    if x[z] != y[z]:
                        count+=1
                
                if count <= 2:
                   
                    union(i,j)
        ans = set()
       

        for key,val in parent.items():
            ans.add(find(val))
        return len(ans) 


                






        
        