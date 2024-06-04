# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]
class Solution:
    
    def __init__(self):
        self.root =TrieNode()
    def insert(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            if not cur.children[ord(word[i]) - ord("a")]:
                cur.children[ord(word[i]) - ord("a")] = TrieNode()
            cur = cur.children[ord(word[i])- ord("a")]
        cur.is_end = True
    def check(self,word,checker):
        cur = cur = self.root
        res = ""
        for i in range(len(word)):
            index = (ord(word[i])- ord("a"))
            if cur.children[index]:
                res+=word[i]
                if res not in checker:
                    return ""
                cur = cur.children[index]
        return word



    def longestWord(self, words: List[str]) -> str:
        for i in words:
            self.insert(i)
        words.sort()
        ans = []
        checker = set(words)
        for i in words:
            x = self.check(i,checker)
            ans.append(x)
      
        ans.sort()
        maxlen = 0
        for  i in range(len(ans)):
            maxlen = max(maxlen,len(ans[i])) 
      
        for j in ans:
            if len(j) == maxlen:
                return j



       
        
        

        




        
        

        