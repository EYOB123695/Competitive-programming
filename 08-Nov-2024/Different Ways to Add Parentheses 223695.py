# Problem: Different Ways to Add Parentheses - https://leetcode.com/problems/different-ways-to-add-parentheses/

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        dict = { 
            "+":lambda x,y: x + y ,
            "-":lambda x,y : x- y ,
            "*":lambda x,y : x *y
        }
        def backtrack(left,right):
            res =  [ ]
            for i in range(left,right +1):
                operator = expression[i]
                if operator in dict:
                    arrone = backtrack(left , i -1)
                    arrtwo = backtrack(i + 1,right)
                    for j in arrone:
                        for k in arrtwo:
                            res.append(dict[operator](j,k)) 
            if res == []:
                res.append(int(expression[left:right + 1]))
            return res
                
        return backtrack(0,len(expression)-1)

        