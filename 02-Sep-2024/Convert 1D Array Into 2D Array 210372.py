# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        matrix = []
        ans =[]
        i = 0
        while i < len(original):
            x = original[i:i+n]
            
            i = i + n 
            matrix.append(x) 
        if len(matrix) == m and len(matrix[0]) == n :
            return matrix
        else:
            return ans
        
        