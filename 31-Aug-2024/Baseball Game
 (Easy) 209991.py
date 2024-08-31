# Problem: Baseball Game
 (Easy) - https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == "C":
                stack.pop()
               
            elif i == "D":
                val = stack[-1]
                stack.append(val * 2)
                
            elif i == "+" :
                currtwo = stack.pop()
                currthree = stack .pop()
                valfour = currtwo + currthree
                stack.append(currthree)
                stack.append(currtwo)
               
                stack.append(valfour) 
                
            else :
                stack.append(int(i))
            
        ans = 0
        while stack:
            ans += stack.pop()
           
        return ans

        


        