# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        if source == destination:
            return True
        for src,dst in edges:
            graph[src].append(dst)
            graph[dst].append(src) 
        queue = deque([source])
        visited = set()
        visited.add(source)
        while queue:
            val = queue.popleft()
            for nei in graph[val] :
                if nei == destination :
                    return True 
                if nei not in visited:
               
                    queue.append((nei)) 
                    visited.add(nei)
        return False

        
        
