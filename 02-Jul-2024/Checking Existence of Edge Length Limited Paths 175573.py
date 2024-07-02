# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        parent = {i:i for i in range(n)}
        rank = [1] * n
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            parx = find(x)
            pary = find(y)
            if parx != pary:
                if rank[parx] > rank[pary]:
                    parent[pary] = parx  
                elif rank[parx] < rank[pary]:
                    parent[parx] = pary 
                else:
                    parent[parx] =  pary 
                    rank[parx] +=1 
        sortedqueries = sorted(enumerate(queries),key = lambda x:x[1][2])
        edgeList.sort(key=lambda x:x[2]) 
        i = 0
        ans = [False] * len(queries)
        for idx,(u,v,limit) in  sortedqueries:
            while i < len(edgeList) and edgeList[i][2] < limit:
                union(edgeList[i][0],edgeList[i][1])
                i+=1
            if find(u) == find(v):
                ans[idx] = True
        return ans
            


  

