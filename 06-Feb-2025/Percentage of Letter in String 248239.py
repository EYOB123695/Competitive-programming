# Problem: Percentage of Letter in String - https://leetcode.com/problems/percentage-of-letter-in-string/description/%20meaning/

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = 0 
        for i in s:
            if i == letter:
                count +=1 
        val =  (count / len(s) ) * 100 
        return int(val)

        