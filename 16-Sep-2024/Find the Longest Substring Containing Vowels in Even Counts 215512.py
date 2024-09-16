# Problem: Find the Longest Substring Containing Vowels in Even Counts - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
    
       
        dict = {0: -1}
       
        bitmask = 0
        ans = 0
        dicttwo = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
      
        max_len = 0
        
      
        for i, char in enumerate(s):
          
            if char in dicttwo:
                bitmask ^= dicttwo[char]
            
           
            if bitmask in dict:
                ans = max(ans, i - dict[bitmask])
            else:
              
                dict[bitmask] = i
        
        return ans






        