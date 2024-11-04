# Problem: Minimum Score Triangulation of Polygon - https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def dfs(i,j):
            res = float("inf")
            for k in range(i+1,j):
                res = min(res,values[i] * values[j] * values[k]  +dfs(i,k) +dfs(k,j))
            if res == float("inf"):
                return 0 
            return res
        return dfs(0,len(values)-1)

        