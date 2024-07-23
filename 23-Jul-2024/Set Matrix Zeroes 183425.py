# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        check = set()
        checktwo = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    check.add(i)
                    checktwo.add(j)
        for  i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in check or j in checktwo:
                    matrix[i][j] = 0
        return matrix



        