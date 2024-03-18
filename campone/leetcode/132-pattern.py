class Solution:
    def find132pattern(self, nums: List[int]) -> bool: 
        stack = []
        m = nums[0] 

        for i in nums[1:]:
            while stack and i >= stack[-1][0]:
                stack.pop()
            if len(stack) > 0 and i > stack[-1][1]:
                return True
            stack.append([i,m])
            m = min(m,i) 
        return False

        