# Problem: Cheapest Flights Within K Stops - https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prev = [float("inf") ] * n 
        prev[src] = 0
        count = 0 
        for i in range(k+1):
            curr = prev[:]
            for u, v , p in  flights :
                if   p + prev[u] < curr[v]:
                    curr[v] = p +prev[u]
                
                
            prev = curr[:]
            
        if prev[dst] == float("inf"):
            return  -1 
        else:
            return prev[dst]
        
