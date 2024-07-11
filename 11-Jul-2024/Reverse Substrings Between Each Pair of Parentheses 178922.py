# Problem: Reverse Substrings Between Each Pair of Parentheses - https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack  = deque()
        res  = []
        for c in s:
            if c =="(":
                stack.append(len(res))
            elif  c ==")":
                x = stack.pop()
                res[x:] = res[x:][::-1]
            else:
                res.append(c)
        return "".join(res)
                

        