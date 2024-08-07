# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
    
       

        dictionarytwo = Counter(word)
        wordcount = sorted(dictionarytwo.items(),key= lambda x:-x[1] )
        
        ans = 0
        x = [1,1,1,1,1,1,1,1]
        idx = 0
        for k ,val in wordcount:
        
            ans += x[idx] *val
            idx += 1 
           
            if idx  >= len(x):
                idx = 0
                x = [count + 1 for count in x] 
            
               
        return ans






        