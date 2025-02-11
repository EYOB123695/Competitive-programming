# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        count = 0 
        for i in range(left,right+1):
            for u,v in ranges:
                if  u <= i   <= v:
                    count += 1 
                    break
                    
        return True if count == (right - left) + 1 else False




        