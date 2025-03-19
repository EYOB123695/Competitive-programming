# Problem: Find Unique Binary String - https://leetcode.com/problems/find-unique-binary-string/description/

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        ans = []
        bucket = []
        check = set(nums)
        def backtrack(i,curr):
            if  i == n:
                bucket = "".join(curr)
                return None if bucket  in check  else bucket
            ans = backtrack(i+1 , curr)
            if ans :
                return ans
            curr[i] = "1"

            ans = backtrack(i+1 ,curr)
            if ans:
                return ans
        return backtrack(0,["0" for i in nums])
                    
            


        