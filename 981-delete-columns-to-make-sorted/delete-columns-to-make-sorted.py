class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        ans = 0 
        for j in range(len(strs[0])):
            val = -float("inf")
            for i in range(len(strs)):
                if val > ord(strs[i][j]) : 
                    ans += 1
                    break


                val = ord(strs[i][j])
        return ans 




        