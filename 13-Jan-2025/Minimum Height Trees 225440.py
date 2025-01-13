# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0] 
        graph = defaultdict(list)
        for src,dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        dic = {}
        leaves = deque()
        for src,nei in graph.items():
            if len(nei) == 1:
                leaves.append(src)
            dic[src] = len(nei)
        while leaves:
            if n <=2 :
                return list(leaves)
            for i in range(len(leaves)):
                node = leaves.popleft()
                n-=1
                for nei in graph[node]:
                    dic[nei]-=1
                    if dic[nei] == 1:
                        leaves.append(nei)

        

        