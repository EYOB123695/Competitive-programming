# Problem: Reshape the Matrix - https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        ans = [[0] * c for i in range( r)]
        if r * c != len(mat) * len(mat[0]):
            return mat
        x= 0  
        y = 0 
        for i in range(len(mat)):
          
            for j in range(len(mat[0])):
                if y == c:
                    x+=1 
                    y = 0
               
                if x < r and y < c:
                    ans[x][y] = mat[i][j]
                y += 1
        return ans

        




        