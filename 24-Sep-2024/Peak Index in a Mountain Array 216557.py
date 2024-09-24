# Problem: Peak Index in a Mountain Array - https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0 
        r = len(arr) -1 

        while l <= r :
            mid = l + (r-l)//2 
            if arr[mid] >arr[mid+1 ]:
               r = mid -1 
            
            else:
                l  = mid + 1
        return l
        
