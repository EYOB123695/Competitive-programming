class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        sum = 0 
        count = 0
        val = float("inf")
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                curr = abs(matrix[i][j])
                sum += curr
                if matrix[i][j] < 0 :
                    count  += 1 
                
              
                val = min(val,curr)
                    
                        

       
        if count % 2 == 0  :
            return sum 
        else :
            return sum + (2 * ( - val)) 

        


        