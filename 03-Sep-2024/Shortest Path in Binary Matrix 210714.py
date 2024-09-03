# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (1, -1),
            (1, 1),
            (-1, 1),
            (-1, -1),
        ]   
       
        def inbound(r,c):
            if 0 <= r < len(grid) and  0 <= c < len(grid[0])  :
                return True
            else :
                return False

        queue = deque([(0, 0)])
      
        
        if grid[0][0] == 1 or grid[-1][-1] == 1 :
            return -1
        grid[0][0] = 1
        while queue:
            row,col = queue.popleft()
            if row == len(grid) - 1 and col == len(grid[0])-1:
                return grid[row][col]

            for r,c in directions:  
                nr = r + row  
                nc   = c  + col
                if inbound(nr,nc) and grid[nr][nc] == 0 :
                    queue.append((nr,nc)) 
                    
                 


                    grid[nr][nc] = grid[row][col] + 1  
                    


        return -1 