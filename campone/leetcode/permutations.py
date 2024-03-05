class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
       res = []
       def backtrack(start,combination):
            if len(combination) >= len(nums) :   
                res.append(combination.copy())
                return  
            for i in range(len(nums)):
                if nums[i] not in combination :      
                    combination.append(nums[i]) 
                    print(combination)
                    backtrack(i+1,combination)
                    combination.pop() 
       backtrack(1,[]) 
       return res    



        