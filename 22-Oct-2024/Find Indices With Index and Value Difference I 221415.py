# Problem: Find Indices With Index and Value Difference I - https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description/

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        ans = [ ]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(nums[i] - nums[j]) >= valueDifference and abs(i - j) >=indexDifference :
                    ans.append(i)
                    ans.append(j)
        if len(ans) < 2 :
            return [-1,-1]
        else:
            return [ans[0] ,  ans[1]]





        