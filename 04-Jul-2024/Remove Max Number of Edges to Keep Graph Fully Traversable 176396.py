# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        a = {i:i for i in range(1,n+1)}
        b = {i:i for i in range(1,n+1)}
        def find(parent,x):
            if parent[x] != x:
                parent[x] = find(parent,parent[x])
            return parent[x]
        def union(parent,x,y):
            parx = find(parent,x)
            pary = find(parent,y)
            if parx != pary:
                parent[parx] = pary 
                return True 
            return False
        edges.sort()
        edges =  edges[::-1]

        count = 0 
        for type,u,v in edges:
            if type == 3:
                if union(a,u,v) and union(b,u,v):
                    count += 1 
            elif type == 1:
                if union(a,u,v):
                    count += 1 
            elif type == 2:
                if union(b,u,v):
                    count +=1 
        setone = set(find(a, i) for i in range(1, n + 1))  
        settwo = set(find(b, i) for i in range(1, n + 1))
        if len(setone) == 1 and len(settwo)  == 1 :
            return len(edges) - count
        else:
            return -1 





            

        


