# Problem: All Ancestors of a Node in a Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        degree = defaultdict(int)
        for i , j in edges:
         
            graph[i].append(j)
            degree[j] += 1 
        
        queue = deque()
        ans = [set() for _ in range(n)] 
        for i in range(n):
            if degree[i] == 0:
                queue.append(i)
      
        while queue:
            val = queue.popleft()
            for neighbour in graph[val]:
                ans[neighbour ].add(val)
                ans[neighbour]  |= ans[val]
                degree[neighbour ] -= 1 
                if degree[neighbour] == 0:
                    queue.append(neighbour)
        ans = list(map(lambda s: sorted(list(s)),ans))
        return ans




        