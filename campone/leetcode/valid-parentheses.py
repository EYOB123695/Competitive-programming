class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(len(s)):
            if s[i] == '{' or s[i] == "[" or s[i]== "(":
                stack.append(s[i])
            if s[i] == "}" or s[i]==")" or s[i] == "]": 
                if len(stack) == 0 :
                    return False
                
                if  (s[i] == "}" and  stack[-1] != "{") or (s[i] == "]" and stack[-1] != "[" ) or (s[i] == ")" and stack[-1] != "("):
                    return False
                stack.pop()

        if  len(stack) == 0:
            return True
        else:
            return False
        
        