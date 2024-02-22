class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n= len(mat)
        m=len(mat[0])
        
        k=len(mat)-1
        sumone=0
        sumtwo=0             
        for i in range(n):
            for j in range(m):
                if i == j :
                    sumone += mat[i][j]
                    
                    
                if i + j == k :

                    sumtwo += mat[i][j]
                    if i == j :
                        sumtwo -= mat[i][j] 
        ans = sumone + sumtwo
        return ans            
        



        