# Problem: Palindrome Number - https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        arr = str(x)
        if "".join(arr) == "".join(arr[::-1]):
            return True 
        else:
            return False
        