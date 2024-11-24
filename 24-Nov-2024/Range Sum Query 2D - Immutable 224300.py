# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        self.prefixsum = [ [0] * (col+1) for r in range(row+1) ]
        for r in range(len(matrix)):
            prefix = 0 
            for c in range(len(matrix[0])):
                prefix += matrix[r][c]
                self.prefixsum[r+1][c+1] = prefix + self.prefixsum[r][c+1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefixsum[row2+1][col2+1] -  self.prefixsum[row1][col2+1] - self.prefixsum[row2+1][col1] + self.prefixsum[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)