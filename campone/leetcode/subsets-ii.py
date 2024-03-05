class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        bucket=[]
        res=set()
        def backtrack(i):
            if i >= len(nums):
                x=(tuple(sorted(bucket)))
               
                res.add(x) 
                return
            bucket.append(nums[i]) 
            backtrack(i+1)
            bucket.pop()
            backtrack(i+1)
        backtrack(0)
        
                      

        return res

             
                



        