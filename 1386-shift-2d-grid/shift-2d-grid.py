class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        matrix = [[0] * n for _ in range(m)]
        total = (n * m) 
        k = k  % total
        for i in range(m):
            for j in range(n):
               flatindex = (i * n) + j
           
               newflatindex = (flatindex + k) % total 
               r = newflatindex // n
               c = newflatindex % n
               matrix[r][c] = grid[i][j]  

        return matrix 



        