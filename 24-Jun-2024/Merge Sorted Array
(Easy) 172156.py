# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
       
        g = m + n - 1
        m -= 1
        n -= 1

        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[g] = nums1[m]
                m -= 1
            else:
                nums1[g] = nums2[n]
                n -= 1
            g -= 1

        
        while n >= 0:
            nums1[g] = nums2[n]
            n -= 1
            g -= 1
        