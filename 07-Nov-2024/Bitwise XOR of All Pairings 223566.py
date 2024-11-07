# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = len(nums1)
        m = len(nums2)
        ans = 0
        anstwo = 0 
        
        for i in range(n):
            if m % 2 != 0 :
                ans ^= nums1[i]
        for j in range(m):
            if n % 2 != 0:
               
                anstwo ^= nums2[j]
        
        return ans ^ anstwo
            




        