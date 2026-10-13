class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        total_sum = 0
        min_abs = float('inf')
        neg_count = 0
        
        for row in matrix:
            for val in row:
                if val < 0:
                    neg_count += 1
                abs_val = abs(val)
                total_sum += abs_val
                if abs_val < min_abs:
                    min_abs = abs_val
                    
        # If there is an odd count of negatives, one smallest element must stay negative
        if neg_count % 2 != 0:
            total_sum -= 2 * min_abs
            
        return total_sum
        