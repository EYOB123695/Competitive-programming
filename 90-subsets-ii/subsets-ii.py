class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        
        
        result = []
        path = []
        nums.sort()
    
        def backtrack(idx):
            if len(nums) <= idx:
                if not path in result:
                    result.append(path[:])
                return
            path.append(nums[idx])
            backtrack(idx + 1)
            path.pop()
            backtrack(idx + 1)
    
        backtrack(0)
        return result

        