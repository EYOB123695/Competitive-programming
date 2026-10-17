class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n: int) -> int:
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s

        n = len(nums)
    
        # Store: ((digit_sum, value), original_index)
        # Tie-breaking typically uses the value nums[i]
        indexed_arr = [((digit_sum(val), val), i) for i, val in enumerate(nums)]
    
        # Sort to find where each element belongs
        indexed_arr.sort(key=lambda x: x[0])
    
        visited = [False] * n
        swaps = 0
    
        for i in range(n):
            # Already visited or already in the correct sorted spot
            if visited[i] or indexed_arr[i][1] == i:
                continue
        
            # Traverse the cycle
            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = indexed_arr[curr][1]
                cycle_size += 1
            
            if cycle_size > 1:
                swaps += cycle_size - 1
            
        return swaps
        