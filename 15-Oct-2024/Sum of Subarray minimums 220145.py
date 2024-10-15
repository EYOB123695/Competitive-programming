# Problem: Sum of Subarray minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        Mod = 10 ** 9+ 7 
        res = 0 
        stack = []
        for i,n in enumerate(arr):
            
            while stack and stack[-1][1] > n:
                j, m = stack.pop()
                right = i - j 
                left = j - stack[-1][0] if stack else j + 1

                res =  (res  + m * left * right)  % Mod
            stack.append((i,n)) 
        for i in range(len(stack)):
            j,m = stack[i]
            left  = j - stack[i-1][0] if i != 0  else j +1 
            right = len(arr) - j 
            res =  (res  + m * left * right)  % Mod
        return res 

            
            

        



        