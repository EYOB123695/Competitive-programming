# Problem: Vowel of All Substring - https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        vowelletters = ["a","e","i","o","u"]
        vowel = set(vowelletters)

        ans = 0 
        n = len(word)
        for i in range(len(word)) :
            if word[i] in vowel:
                ans += (i + 1 ) * (n - i) 
        return ans






        