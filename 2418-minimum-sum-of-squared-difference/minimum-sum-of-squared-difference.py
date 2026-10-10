class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        k = k1 + k2
        
        # Calculate absolute differences
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        total_diff = sum(diffs)
        
        # If total k covers all differences, we can reduce all to 0
        if total_diff <= k:
            return 0
        
        max_val = max(diffs)
        count = [0] * (max_val + 1)
        for d in diffs:
            count[d] += 1
            
        # Greedily reduce the largest differences
        for v in range(max_val, 0, -1):
            if count[v] == 0:
                continue
            if k == 0:
                break
                
            take = min(k, count[v])
            count[v] -= take
            count[v - 1] += take
            k -= take
            
            # If k is still > 0, all count[v] moved to v - 1, 
            # and the loop will process v - 1 in the next step.
            
        # Calculate sum of squared differences
        ans = 0
        for v in range(1, max_val + 1):
            if count[v] > 0:
                ans += count[v] * (v * v)
                
        return ans
        