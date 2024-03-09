class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack =[ ]
        res = [-1] *len(nums1)
        nums1idx = {}
        for i, n in enumerate(nums1):
            nums1idx[n] = i
        ans = [-1] * len(nums1)
        for i in range(len(nums2)):
            cur =nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums1idx[val]
                res[idx]=cur
            if cur in nums1idx:
                stack.append(cur) 
        return res



        