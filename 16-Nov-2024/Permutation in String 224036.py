# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        r = k 
        dictionary = Counter(s1)
        dicttwo = Counter(s2[:k])
        if len(s1) > len(s2):
            return False
        elif len(s1) == len(s2):
            return dictionary == dicttwo
        
        
        l = 0 
        while r < len(s2):
            if dictionary == dicttwo :
                return True 
           
        
            dicttwo[s2[r]] += 1 
            r += 1 
           
            
            dicttwo[s2[l]] -= 1 
            l += 1   
        return  dictionary == dicttwo
            
        




        
        