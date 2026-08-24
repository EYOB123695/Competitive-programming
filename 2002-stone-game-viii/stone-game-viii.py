class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:

        # Prefix sums represent the score gained by taking all elements up to index i
        prefix_sums = list(accumulate(stones))
        n = len(stones)

        # dp represents the maximum relative score difference a player can get
        # Starting from the rightmost full-prefix state:
        dp = prefix_sums[-1]

        # Iterate backwards from the second-to-last stone down to the second stone (index 1)
        for i in range(n - 2, 0, -1):
            dp = max(dp, prefix_sums[i] - dp)

        return dp   