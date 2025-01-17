# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
     
        dictionary={}
        for index,element in enumerate(nums):
            dictionary[element]=index
        for  curr ,new in operations:
            index=dictionary[curr]
            nums[index]=new
            del dictionary[curr]
            dictionary[new]=index

        return nums





        
        