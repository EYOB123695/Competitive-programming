# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float("inf") ]*n for i in range(n) ]
        graph = defaultdict(list)
        for i in range(n):
            dist[i][i] = 0 
        for src,dst,price in edges:
            dist[src][dst] = price 
            dist[dst][src] = price 
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j],dist[i][k] + dist[j][k]) 
        for i in range(n):
            for j in range(n):
                if dist[i][j] <=distanceThreshold:
                    if j not in graph[i]:
                        graph[i].append(j)
                    if i not in graph[j]:
                        graph[j].append(i) 
        ans = []
        count = float("inf")
        for  k ,val in graph.items():
            count = min(count,len(val))
        for k,val in graph.items():
            if len(val) == count:
                ans.append(k)
        return ans[-1]


            


        
        
        





        