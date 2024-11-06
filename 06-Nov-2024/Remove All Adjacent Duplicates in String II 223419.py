# Problem: Remove All Adjacent Duplicates in String II - https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        dictionary = defaultdict(int)
        count = 1 
        for i in s:
            if stack and stack[-1][0] == i:
                stack[-1] = (i , stack[-1][1] + 1)
            
                if stack[-1][1] == k:
                   stack.pop()
            else:
                stack.append((i,1))
              
        ans = []
        for k in stack:
            ans.append(k[0] * k[1])
        return "".join(map(str,ans))
        
        
        
        
        
        
        

        
        
        
        
        
        

        

    
        
        



    








        