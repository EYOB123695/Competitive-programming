# Problem: Left-and-right-sum-differences - https://leetcode.com/problems/left-and-right-sum-differences/

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        prefixsum = [0] * len(nums)
        prefixsumtwo  = [0] * len(nums)
        print(prefixsum)
        print(prefixsumtwo)
        for i in range(len(nums)-1):
            prefixsum[i+1] = prefixsum[i] + nums[i]
        for i in range(len(nums)-1,0,-1):
            prefixsumtwo[i-1] = prefixsumtwo[i] + nums[i] 
        ans = []
        print(prefixsum)
        print(prefixsumtwo)
        for i in range(len(prefixsum)):
            ans.append (abs((prefixsum[i]-prefixsumtwo[i])))
        return ans        
        