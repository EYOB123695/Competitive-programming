# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int: 
        visited = set()
        stack = []
        directions  = [(0,1),(1,0) ,(-1,0), (0,-1)]
        def inbound(r,c):
            return 0 <= r < len(grid) and 0<= c < len(grid[0])
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    stack.append((i,j))
                    visited.add((i,j))
                    break 
        perimeter = 0
        while stack :
            i, j  = stack.pop()
            for r,c in directions:
                nr ,nc = r +  i , c + j 
                if not inbound(nr,nc) or grid[nr][nc] == 0 :
                    perimeter +=1 
                elif (nr,nc) not in visited and   grid[nr][nc] == 1:
                    visited.add((nr,nc))
                    stack.append((nr,nc))
            

                
        return perimeter


 


        