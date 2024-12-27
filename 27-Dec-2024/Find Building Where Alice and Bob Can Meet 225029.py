# Problem: Find Building Where Alice and Bob Can Meet - https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        result = [-1] * len(queries)
        dict = defaultdict(list)
        for i, q in enumerate(queries):
            l,r = sorted(q)
            if l == r or  heights[l] < heights[r] :
                result[i] = r 
            else:
                h = max(heights[l] , heights[r])
                dict[r].append((h, i ))
        min_heap = []
        for i , h in enumerate(heights):
            for x , y in dict[i]:
                heapq.heappush(min_heap , (x,y))
            while min_heap and h > min_heap[0][0]:
                x, idx = heapq.heappop(min_heap)
                result[idx] = i 
        return result
        


       