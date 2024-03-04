class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n= len(candidates)
        res=set()

        
        
        def backtrack(start,combination):   
            val = None 
        

        
            if sum(combination) == target :   
                x=(tuple(sorted(combination)))
               
                res.add(x)
                return  
            if sum(combination) > target:
                return
            for i in range(start,n):  
                if val != candidates[i]:
                    
                    combination.append(candidates[i])
                    backtrack(i+1,combination)
                    val=combination.pop()  
        backtrack(0,[]) 
        
        return res
       
        