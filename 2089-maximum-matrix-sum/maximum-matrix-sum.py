class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        total_sum = 0
        min_abs_val = float('inf')
        negative_count = 0

        for row in matrix:
            for val in row:
                if val < 0:
                    negative_count += 1
                
                abs_val = abs(val)
                total_sum += abs_val
                if abs_val < min_abs_val:
                    min_abs_val = abs_val

        # If the number of negatives is odd, the smallest absolute value must remain negative
        if negative_count % 2 != 0:
            total_sum -= 2 * min_abs_val

        return total_sum
        