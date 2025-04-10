# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        res = set()
        l = 0 
        
        for i in range(l,len(s)):
                while s[i] in res:
                    res.remove(s[l])
                    l+=1
                res.add(s[i])
                answer = max(answer , i - l + 1)
        return answer

            



            


        