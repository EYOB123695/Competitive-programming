# Problem: Number of Closed Islands - https://leetcode.com/problems/number-of-closed-islands/

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        answer = 0 
        directions = [(0,1) ,(1,0) , (-1,0) ,(0,-1) ]
        def inbound(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        def dfstwo(r,c):
            grid[r][c] = 1
            for i , j in directions:
                nr, nc = i + r , j + c 
                if inbound(nr,nc) and grid[nr][nc] == 0:
                   
                    dfstwo(nr,nc)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 :
                    if i == len(grid)-1 or i == 0 or j == len(grid[0]) -1 or j == 0 :

                        dfstwo(i,j)

        def dfs(r,c):
            for  i,j in directions:
                nr,nc = r + i , j + c 
                if inbound(nr,nc) and   grid[nr][nc] == 0:
                    
                    grid[nr][nc] = 1 
                    dfs(nr,nc)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 :
                    dfs(i,j) 
                    answer += 1 
        return answer
        




        