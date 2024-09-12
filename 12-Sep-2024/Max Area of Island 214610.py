# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def inbound(r,c):
            return 0<= r < len(grid) and 0<= c < (len(grid[0]))
        directions = [(0,1),(1,0),(-1,0) , (0,-1)]
        
        def dfs(r,c,):
            ans[0]  +=  1
            print(ans)
            
            grid[r][c] = 0 
            for i , j in directions:
                nr,nc = r + i , c + j 
                if inbound(nr,nc) and grid[nr][nc] == 1 :
                   
                    print(nr,nc)
                    dfs(nr,nc) 
            return ans

            
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])) :
                if grid[i][j] == 1:
                    ans = [0]
                    val = dfs(i,j)
                    count =  max(count ,val[0] )
        return count






        