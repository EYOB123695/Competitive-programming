# Problem: Longest Palindrome - https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        dictionary = Counter(s)
        count = 0
        flag = False
        for i,val in dictionary.items():
            if val % 2 == 0:
                count+= val
            if val % 2 != 0:
                count += val - (val % 2)
            if val == 1 or val % 2 == 1:
                flag = True
            if val == len(s):
                return val

        if flag:
            return count + 1
        else:
            return count

        
        