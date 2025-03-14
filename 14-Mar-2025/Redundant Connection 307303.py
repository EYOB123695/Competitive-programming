# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        output = []
        parent = {i:i for i in range(1,n+1)}
        ans= [[]]
        def find(x):
            while x != parent[x]:
                parent[x]= parent[parent[x]]
                x = parent[x]
            return x


        def union(x,y):
           
            parx= find(x)
            pary = find(y)
           
            if parx == pary:
                ans[0] = [x,y]
            else:
                parent[parx]  = pary 
    
        for i in range(len(edges)) : 
            union(edges[i][0],edges[i][1])



        
        
        return ans[0]
                




       



         
        
        




       
        
            











        





        


        
        