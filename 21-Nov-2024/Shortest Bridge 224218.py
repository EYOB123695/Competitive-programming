# Problem: Shortest Bridge - https://leetcode.com/problems/shortest-bridge/

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        visited = set()
        def inbound(r,c):
            return 0<= r < n and 0<= c < m 
        directions = [(0,1) , (1, 0) , (-1,0) , (0, -1 )]
        def dfs(r,c):
            for i , j in directions:
                nr, nc = i + r , j + c 
                if inbound(nr,nc) and grid[nr][nc] == 1  and (nr,nc) not in visited  :
                    visited.add((nr,nc)) 
                    dfs(nr,nc)
        def bfs():
            res, queue  = 0 , deque(visited)
            while queue:
                for i in range(len(queue)):
                    r,c = queue.popleft()
                    for i , j in directions:
                        nr , nc = i + r , j + c 
                        if inbound(nr,nc) and  grid[nr][nc] == 1 and( nr, nc) not in visited:
                            return res 
                        if inbound(nr,nc) and grid[nr][nc] ==  0  and (nr,nc) not in visited : 
                            queue.append((nr,nc))
                            visited.add((nr,nc))
                res += 1 


            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 :
                    visited.add((i,j))
                    dfs(i,j)
                    print(visited)
                    return bfs()









        