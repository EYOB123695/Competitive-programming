class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        province = 0
        directions = [(0,1) ,(0,-1),(1,0),(-1,0)]
        def inbound(i,j):
            if (i < 0 or i >= len(grid) ) or  (j < 0 or j >= len(grid[0])) :
                return False 
            return True 
        def dfs(i,j):
         
            grid[i][j] = "0"         
            for x,y in directions :
                nr,nc  = x + i, y + j 
                if inbound(nr,nc) and grid[nr][nc] == "1" :
                  
                    dfs(nr,nc)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
            
                if grid[i][j] == '1':
                    province += 1 
                    dfs(i,j)
        return province

           








        