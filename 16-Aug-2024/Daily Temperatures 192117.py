# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack  = [[temperatures[0],0]]

        ans = [0] *len(temperatures)
        for i in range(1,len(temperatures)):
            
            while stack and stack[-1][0] < temperatures[i]:
                
                val =stack.pop()
                ans[val[1]] = i - val[1] 
                
                
                
            stack.append([temperatures[i],i])
        return ans
        







            


            

            





        