# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u , v , w in times:
            graph[u].append((v,w))
        heap = [(0,k)]
        processed = set()
        distance = { i :float("inf") for i in range(1,n+1)}
        distance [k] =  0 
        while heap:
            dist , node =  heapq.heappop(heap)
            if node in processed:
                continue
            processed.add(node)
            for child , weight in graph[node]:
                if weight + dist < distance[child]:
                    distance[child] = weight + dist 
                    heapq.heappush(heap,(weight + dist, child))
        ans = -float("inf")
        for k ,v in distance.items():
            if v == float("inf"):
                return -1 
            ans = max(v,ans)
        return ans

        



             


        