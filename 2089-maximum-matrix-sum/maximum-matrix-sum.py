class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        sum = 0 
        count = 0
        val = float("inf")
        flag = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                sum += abs(matrix[i][j])
                if matrix[i][j] < 0 :
                    count  += 1 
                
                elif matrix[i][j] == 0 :
                    flag = True
                val = min(val,abs(matrix[i][j]))
                    
                        

       
        if count % 2 == 0 or flag :
            return sum 
        else :
            return sum + (2 * ( - val)) 

        


        