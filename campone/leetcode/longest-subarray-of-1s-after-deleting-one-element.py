class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        ans = 0
        res = 0 
        countzeros = 0
        while right < len(nums): 
            if nums[right] == 0 :
                countzeros+=1
            while countzeros > 1: 
                if nums[left] == 0:
                    countzeros -=1 
                
                left+=1 
            ans =right - left 
            res = max(ans,res)
            
            right+=1 
        return res




        