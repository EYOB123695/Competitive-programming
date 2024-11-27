# Problem: Maximum Number of Points with Cost - https://leetcode.com/problems/maximum-number-of-points-with-cost/

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        row = points[0]
        m = len(points[0]) 
        n = len(points)
        for r in range(1,n):
            nextrow = points[r].copy()
            leftrow , rightrow = [0] * m , [0] * m
            leftrow[0] = row[0]
            for i in range(1, m):
                leftrow[i] = max(row[i] , leftrow[i-1] - 1)
            rightrow[-1] = row[-1] 
            for j in range(m - 2 , -1 ,-1):
                rightrow[j] = max(row[j] , rightrow[j + 1] - 1)
            for i in range(len(nextrow)):
                nextrow[i] += max(leftrow[i] , rightrow[i])
            row = nextrow
        return max(row)





        
        
        