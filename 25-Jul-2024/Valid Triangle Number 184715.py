# Problem: Valid Triangle Number - https://leetcode.com/problems/valid-triangle-number/

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        n = len(nums)
        
        
        for k in range(n-1,1,-1):     
            i,j = 0,k-1
            while i < j:
                if nums[i] + nums[j] > nums[k] :
                    ans+= j-i
                    j-=1
                else:
                    i+=1
        return ans

        