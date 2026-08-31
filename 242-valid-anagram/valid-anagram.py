class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictone = Counter(s)
        dicttwo = Counter(t) 
        if dictone == dicttwo :
            return True 
        else : 
            return False  

        