# Problem: As Far from Land as Possible - https://leetcode.com/problems/as-far-from-land-as-possible/description/

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # def inbound(r, c):
        #     return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        # directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # queue = deque()

        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 1:
        #             queue.append((i, j))

        # if len(queue) == 0 or len(queue) == len(grid) * len(grid[0]):
        #     return -1

        # max_dist = -1

        # while queue:
        #     r, c = queue.popleft()

        #     for i, j in directions:
        #         nr, nc = r + i, c + j
        #         if inbound(nr, nc) and grid[nr][nc] == 0:
        #             grid[nr][nc] = grid[r][c] + 1
        #             max_dist = grid[nr][nc] - 1
        #             queue.append((nr, nc))

        # return max_dist
        def inbound(r,c):
            return 0 <= r <  len(grid) and 0 <= c < len(grid[0])
      
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])) :
                if grid[i][j] == 1:
                    queue.append((i,j))

        if len(queue) == 0 or len(queue) == len(grid) * len(grid):
            return -1
        
        dist = -float("inf")
       
        
        while queue:
            r,c = queue.popleft()
         
            
            for i,j in directions:
                    nr,nc = i + r , c + j 
                    if inbound(nr,nc) and grid[nr][nc] == 0:
                        grid[nr][nc] = grid[r][c] + 1
                        dist = max(dist,grid[nr][nc] -1)
                        queue.append((nr,nc))

        return dist





        

        