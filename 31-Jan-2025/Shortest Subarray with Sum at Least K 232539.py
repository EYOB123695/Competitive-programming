# Problem: Shortest Subarray with Sum at Least K - https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        length = float("inf")
        queue = deque()
        sum = 0
        for right in range(len(nums)):
            sum += nums[right]
            if sum >= k:
                length = min(length,right + 1 )
            while queue and sum - queue[0][0] >= k:
                prefix,end_idx = queue.popleft()
                length = min(length, right - end_idx)
            while queue and queue[-1][0] >= sum:
                queue.pop()
            queue.append((sum,right))
        return -1 if length == float("inf") else length













        



        