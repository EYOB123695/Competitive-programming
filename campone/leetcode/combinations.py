class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start,combination):
            if len(combination) == k :
                res.append(combination.copy())
                return 
            for i in range(start,n+1):
                combination.append(i)
                backtrack(i+1,combination)
                combination.pop() 
        backtrack(1,[])
        return res

