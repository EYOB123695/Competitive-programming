# Problem: Find the Smallest Divisor Given a Threshold - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l=1
        h=max(nums)
        ans=h
        while l <= h:
            c= 0
            mid=l + (h - l) // 2

            for i in nums:
                c += -(- i//mid)
            if c <= threshold:
                if mid <ans:
                    ans=mid 
                h = mid-1
                               
            else:
                 l = mid+1
        return ans
        