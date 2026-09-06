class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0

        # dp[j] stores the number of subsequences of s that equal t[:j]
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty target string has 1 match

        for char_s in s:
            # Traverse backwards to preserve previous row results
            for j in range(n, 0, -1):
                if char_s == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]
        