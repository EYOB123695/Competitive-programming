class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        # Precompute suffix sums
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        memo = {}
        
        def solve(i: int, M: int) -> int:
            if i >= n:
                return 0
            if i + 2 * M >= n:
                return suffix_sum[i]
            if (i, M) in memo:
                return memo[(i, M)]
            
            max_stones = 0
            for X in range(1, 2 * M + 1):
                max_stones = max(max_stones, suffix_sum[i] - solve(i + X, max(M, X)))
                
            memo[(i, M)] = max_stones
            return max_stones

        return solve(0, 1)
        

        