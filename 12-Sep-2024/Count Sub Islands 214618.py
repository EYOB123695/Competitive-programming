# Problem: Count Sub Islands - https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def inbound(r,c):
            return 0<= r < len(grid2) and 0<= c<len(grid2[0]) 
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        
        def dfs(r,c):
            
            
            grid2[r][c] = 0
            if grid1[r][c] == 0:
                ans[0] = False
            for i,j in directions:
                nr,nc = i + r, c + j
                if inbound(nr,nc) and grid2[nr][nc] == 1 :
                     dfs(nr,nc)
            return ans[0]


        count = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1 :
                    ans = [True]
                    if  dfs(i,j):
                        count += 1 
        return count

        