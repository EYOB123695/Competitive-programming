# Problem: Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dictone = Counter(nums1)
        dicttwo = Counter(nums2)
        ans =[]
        for i in nums1:
            if dicttwo[i] > 0:
                dicttwo[i] -= 1
                ans.append(i) 
        return ans


            

        