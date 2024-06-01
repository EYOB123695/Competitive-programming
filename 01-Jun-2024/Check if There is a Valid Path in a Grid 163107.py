# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        up = {x :set([2,3,4]) for x in [2,5,6]}
        down = {x :set([2,5,6]) for x in [2,3,4]}
        left = {x :set([1,4,6]) for x in [1,3,5]}
        right = {x :set([1,3,5]) for x in [1,4,6]}
        directions = [(-1,0,up) ,(1,0,down),(0,-1,left),(0,1,right)]

        n = len(grid)
        m = len(grid[0])
        def inbound(i,j):
            return 0 <= i < n and 0 <= j < m

        


        
        visited = set()
        stack = [(0,0)]
        def dfs():
            while stack:
                i,j = stack.pop()
                visited.add((i,j))
                if i == n-1 and j == m-1:
                    return True
                for r,c,d in directions:
                    nr,nc = i+r, j+ c
                    if inbound(nr,nc) and (nr,nc) not in visited :
                        if grid[i][j] in d and grid[nr][nc] in d[grid[i][j]] :
                            
                            stack.append((nr,nc))
            return False
        return(dfs())

            





        
            