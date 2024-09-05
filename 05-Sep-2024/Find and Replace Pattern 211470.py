# Problem: Find and Replace Pattern - https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]: 
        def check(word,pattern):
            dictone = {}
            dicttwo = {}
            for i,j in zip(word,pattern):
                if i not in dictone :
                    dictone[i] = j
                if j not in dicttwo :
                    dicttwo[j]  = i 
                if dictone[i] != j or dicttwo[j] != i:
                    return False 
            return True 
        arr =  []
        for i in words:
            if check(i,pattern):
                arr.append(i)
        return arr



        