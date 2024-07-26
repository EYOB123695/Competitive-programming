# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        arr = []
        for i,n in enumerate(nums):
            n = str(n)
            check = 0
            for c in n:
                check *= 10
                check +=  mapping[int(c)]
            arr.append((check,i))
        arr.sort()
        return [nums[a[1]] for a in arr] 
               


       