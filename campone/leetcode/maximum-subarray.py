class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxval=nums[0]
        sum=0
        for n in nums:
            if sum < 0 :
                sum=0
            sum+=n
            maxval=max(sum,maxval)
        return maxval

        