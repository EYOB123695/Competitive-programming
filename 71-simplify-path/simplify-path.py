class Solution:
    def simplifyPath(self, path: str) -> str:
        stack  = [ ]
        curr = ""
        for i in path + "/" :
            if i == "/" :
                if curr == "..":
                    if stack: 
                     stack.pop()
                elif curr != "" and curr != ".":
                    stack.append(curr)
                
                curr = ""  
            else : 
                curr += i 
        return "/" + ("/").join(stack)
               
                 

        