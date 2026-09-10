class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx,val in enumerate(nums):
            if target - nums[idx] in seen :
                return [seen[target- nums[idx]], idx]
            seen[val] = idx 
        

            

            




     




            






        
        