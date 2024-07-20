# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row = len(dungeon)
        col = len(dungeon[0])
        dp= [[0]*(col) for i in range(row)]
        for  i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                if i == row-1 and j == col-1:
                    dp[i][j]=min(0,dungeon[i][j]) 
                elif i == row-1:
                    dp[i][j] = min(0,dungeon[i][j]+dp[i][j+1]) 
                elif j == col-1:
                     dp[i][j] = min(0,dungeon[i][j]+dp[i+1][j])
                else:
                    dp[i][j] = min(0,dungeon[i][j]+max(dp[i+1][j],dp[i][j+1]))
        return abs(dp[0][0]) +1
        