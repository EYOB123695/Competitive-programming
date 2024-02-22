class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        stack=[] 
        ans= [0] * n  
        for i  in range(len(temperatures)):
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i] :
                l = stack.pop()
                k = i-l
                ans[l] = k 
            stack.append(i)
        return ans   
        
        