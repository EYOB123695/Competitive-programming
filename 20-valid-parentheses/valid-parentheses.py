class Solution:
    def isValid(self, s: str) -> bool:
        dict = {")" : "(" , "}" :"{" , "]" : "[" } 
        stack = [ ]
        closing = set(["}", "]", ")"])
        for i in s : 
            if i  in closing and stack:
                if stack[-1] != dict[i] : 
                    return False 
                stack.pop()
            else: 
                stack.append(i)
        return True if not stack else False
            