# Problem: Maximum Sum With Exactly K Elements  - https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        heap = []
        
        ans = 0 
        count = 0
        for i in nums:
            heap.append(-1 * i)
        heapq.heapify(heap)
      
        while count < k: 

            val =  heapq.heappop(heap)
            print(val)
            ans += ( -1 * val) 
            heapq.heappush(heap,((val - 1 )))
         
            count += 1 
            
        return ans
            





        