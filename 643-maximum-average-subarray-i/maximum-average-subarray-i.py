class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = sum(nums[:k])
        l = 0
        curr = ans 
        for r in range(k,len(nums)):
            
            curr += nums[r]
            curr -= nums[l]
            ans = max(ans,curr)
            
            l += 1
        return ans / k









        