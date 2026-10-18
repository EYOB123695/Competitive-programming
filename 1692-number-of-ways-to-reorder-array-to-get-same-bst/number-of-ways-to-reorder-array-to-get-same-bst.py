class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        def count_ways(arr: list[int]) -> int:
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            
            ways_left = count_ways(left)
            ways_right = count_ways(right)
            
            # Number of ways to interleave left and right elements
            interleave = comb(len(left) + len(right), len(left)) % MOD
            
            return (interleave * ways_left * ways_right) % MOD

        # Subtract 1 to exclude the original array order
        return (count_ways(nums) - 1) % MOD
        