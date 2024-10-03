# Problem: Make Sum Divisible by P   - https://leetcode.com/problems/make-sum-divisible-by-p/

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        if sum(nums) % p ==0 :
            return 0 
        remain = sum(nums) % p 
        ans  = len(nums)
        
        curr = 0 
        dict = {0:-1 }
        for idx,i in enumerate(nums):
            curr = (curr + i)% p
            prefix = (curr - remain + p) % p
            if prefix in dict:
                length = idx - dict[prefix]
                ans = min(ans,length)
            dict[curr] =  idx 
        return -1 if ans == len(nums) else ans