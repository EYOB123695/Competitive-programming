# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        
           
        parent = {i:i for i in range(n)}

        rank  = [1] * n
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  
            return parent[x] 
        def union(x,y):
            parx = find(x)
            pary = find(y)
            if parx != pary :
                if rank[parx] > rank[pary]:
                    parent[pary] = parent[parx] 
                    
                elif rank[parx] < rank[pary]:
                    
                    parent[parx] = parent[pary] 
                else:

                    parent[pary] = parx 
                    rank[parx] += 1
        for e,v in edges: 
            union(e,v) 
        
        dictionary =defaultdict(int)
        for i in range(n):
            x = find(i)
            dictionary[x] += 1
        count = 0
        for k,v in dictionary.items():
            count += v * (n - v)
        return count // 2
