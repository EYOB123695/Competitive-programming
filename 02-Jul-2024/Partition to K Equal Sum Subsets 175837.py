# Problem: Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        used = [False] * len(nums)
        target = sum(nums) / k 
        nums = nums[::-1]
        def backtrack(i,sum,k):
            if k == 0:
                return True 
            if sum > target:
                return False
            
            if sum == target:
                return backtrack(0,0,k-1)
            for j in range(i,len(nums)):
                if used[j] :
                    continue
                used[j] = True
                if backtrack(j+1,sum+nums[j],k):
                    return True 
                used[j] = False
                if sum == 0:
                    break
            return False
        return backtrack(0,0,k)
       
             

        
        