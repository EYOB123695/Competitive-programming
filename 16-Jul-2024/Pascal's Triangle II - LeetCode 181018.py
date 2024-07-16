# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for i in range(rowIndex):
            row = [0] * (len(ans)+ 1)
            for j in range(len(ans)):
                row[j] += ans[j]
                row[j+1] += ans[j]
            ans = row
        return ans