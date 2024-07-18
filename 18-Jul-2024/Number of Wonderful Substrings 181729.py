# Problem: Number of Wonderful Substrings - https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        ans = 0
        dictionary = {}
        dictionary[0] = 1
        mask = 0
        check = [ord(i) - ord("a") for  i in word]
        for i in check:
            mask ^= (1<<i)
            
            if mask in dictionary :
                ans += dictionary [mask]
                dictionary [mask] +=1 
            else:
                dictionary[mask] = 1 
            for j in range(10):
                if mask ^ (1<<j) in dictionary :
                    ans += dictionary [ mask^ (1<<j)] 
        return ans



        




        
