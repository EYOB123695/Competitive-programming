# Problem: Minimum Number of Days to Make m Bouquets - https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def check(mid):
            count = 0 
            res = 0
            for j in range(len(bloomDay)):
                if bloomDay[j] <= mid:
                    count +=1 
                    if count == k:
                        count = 0 
                        res +=1 
                else:
                    count  = 0 
            return res >= m
        if len(bloomDay) < (m * k) :
            return -1
        l = min(bloomDay)
        r = max(bloomDay)
   
        while l < r :
            mid = l +(r-l) //2 
            if check(mid):
                r =  mid 
               
            else:
                l = mid +1 
        return l