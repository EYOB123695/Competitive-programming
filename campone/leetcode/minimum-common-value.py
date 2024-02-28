class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        r=0
        l=0
        n = len(nums1)
        m = len(nums2) 
        while r < n and l < m: 
            
            if nums1[r] == nums2[l]:
                return nums1[r]
                r+=1
                l+=1
            if nums1[r] < nums2[l]:
                r+=1
            else :
                l+=1 
        return -1
        