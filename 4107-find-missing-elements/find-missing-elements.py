class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans =[]
        for i in range(len(nums)-1):
            val = 0
            diff = nums[i+1] - nums[i] -1 
            while nums[i] + 1 != nums[i+1] :
                
                diff -= 1
                val = val + 1 
                ans.append(nums[i] + val)
                if diff == 0:
                    break

        return ans 



        