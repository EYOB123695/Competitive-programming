class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]: 
        
        n= len(candidates)
        res = []
        def backtrack(start,combination):
            if sum(combination) == target :   
                res.append(combination[:])
                return  
            if sum(combination) > target:
                return
            for i in range(start,n):          
                combination.append(candidates[i])
                backtrack(i,combination)
                combination.pop()  
        backtrack(0,[]) 
        return res     
        
    