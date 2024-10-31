# Problem: Max Increase To Keep City Skyline - https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ans = 0 
        n = len(grid)
        m = len(grid[0])
        maxr = []
        maxc = []
        
 
        for i in range(n):
            val = 0
            for j in range(m):
                val = max(val,grid[i][j])
            maxr.append(val)
        for i in range(m):
            val = 0
            for j in range(n):
                val = max(val,grid[j][i])
            maxc.append(val)
        for i in range(n):
            for j in range(m):
                ans += (abs(grid[i][j] - min(maxr[i],maxc[j])))
        return ans


                


                


        
        