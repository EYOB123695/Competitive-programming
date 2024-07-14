# Problem: Merge Strings Alternately - https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        r = 0
        ans = ""
        while l < len(word1) and r< len(word2):
            ans = ans + word1[l]
            ans = ans + word2[r] 
            l+=1
            r+=1
        while l <= len(word1) -1 :
            ans = ans + word1[l]
            l+=1
        while r <= len(word2)-1: 
            ans = ans + word2[r]
            r+=1
        return ans
        
        return ans

        