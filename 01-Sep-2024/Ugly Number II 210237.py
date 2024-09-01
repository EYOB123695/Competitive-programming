# Problem: Ugly Number II - https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i  = 0 
        heap = [1]
        check = set() 
        factors = [2,3,5]
        for i in range(n):
            val = heapq.heappop(heap)
            if  i == n-1 :
                return val
            
            for i in factors:
                if val * i not in check:
                    x  = val *i 
                    check.add(x)
                    heapq.heappush(heap,x) 
        return val



        