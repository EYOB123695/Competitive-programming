class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        arr = [] 
        r = len(nums) -1 
        for i in range(len(nums)):
            arr.append([nums[i], i])
        arr.sort()

        while l < r :  
            if (arr[l][0] + arr[r][0]) == target : 
                return [arr[l][1],arr[r][1]]
            elif arr[l][0] + arr[r][0] > target : 
                r -= 1 
            else :
                l += 1
        
        