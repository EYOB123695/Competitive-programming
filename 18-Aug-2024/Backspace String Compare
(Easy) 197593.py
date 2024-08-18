# Problem: Backspace String Compare
(Easy) - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack  = []
        stacktwo = []
       
        for i in s:
            if i != "#":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
        for j in t:
            if j != "#":
                stacktwo.append(j)
            else:
                if stacktwo:
                    stacktwo.pop()
       
              
        x = "".join(stack[::-1])
        t = "".join(stacktwo[::-1])
      
        if x != t:
            return False
        else:
            return True

        


        