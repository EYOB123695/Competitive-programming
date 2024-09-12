# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = len(words)
        setone = set(allowed)

        
        for i in words :
        
            for j in i :
                if j not in allowed:
                   
                    count -=1 
                    break
           
            
            
        return count




        