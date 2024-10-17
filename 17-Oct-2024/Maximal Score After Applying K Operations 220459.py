# Problem: Maximal Score After Applying K Operations - https://leetcode.com/problems/maximal-score-after-applying-k-operations

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        count = 0 
        ans = 0
        for i in nums:
            heapq.heappush(heap , -1 * i)
        while count < k:
            x = heapq.heappop(heap)
            count += 1 
            ans +=  - 1 *x
            val =  math.ceil( (-1 * x) / 3 ) 
            heapq.heappush(heap, -val )
           
        return ans








        