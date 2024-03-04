class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        bucket = []
        ans = []
        def backtrack(i):
            if i >= len(nums):
                ans.append(bucket.copy())
                
                return 
            bucket.append(nums[i])
            
            backtrack(i+1) 
            bucket.pop()
            backtrack(i+1)
        backtrack(0)
        return ans

            
        
            
            




        