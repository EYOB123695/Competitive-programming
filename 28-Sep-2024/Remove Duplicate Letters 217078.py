# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dicttwo = {val:i for i,val in  enumerate(s)}
        settwo = set(s)
        stack = [ ]
        inset = set()
        for i,char in enumerate(s):
            if char not in inset:
                while stack and char < stack[-1] and i < dicttwo[stack[-1]]:
                    inset.remove(stack.pop())
                stack.append(char)
                inset.add(char)
        return "".join(stack)


            


            






        


        