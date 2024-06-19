# Problem: Find the Difference - https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dictionary = Counter(t)
        for i in s:
            if i  in t:
                dictionary[i] -= 1
                
        for k,v in dictionary.items():
            if v == 1:
                return k
                break



        
        
        