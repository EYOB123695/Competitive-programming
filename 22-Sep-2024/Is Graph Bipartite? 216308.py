# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool: 
        color = [-1] * len(graph)
        n= len(graph)
        def dfs(node):

            for nei in graph[node]:
                if color[nei] == -1 :
                    color[nei]  = 1 - color[node] 
                    if not dfs(nei):
                        return False
                elif color[nei] == color[node]:
                    return False 
            return True

        for i in range(n):
            if color[i] == -1 :
                color[i] = 0
                if not dfs(i):
                    return False
               
        return True


      

       












        