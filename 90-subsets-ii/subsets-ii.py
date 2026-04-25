class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
      
        res = []
        # Step 1: Sort is mandatory to handle duplicates
        nums.sort()
    
        def backtrack(index, path):
            # Every path generated is a valid subset
            res.append(list(path))
        
            for i in range(index, len(nums)):
                # Step 2: Skip duplicates
                # If nums[i] == nums[i-1], it means we already started a 
                # branch with this value at this specific recursion level.
                if i > index and nums[i] == nums[i-1]:
                    continue
            
                # Standard backtracking: Choose, Explore, Un-choose
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
            
        backtrack(0, [])
        return res
        