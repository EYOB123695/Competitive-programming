# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dictionary = Counter(nums)
        ans = []
      
        for k , val in dictionary.items():
            if val == 2:
                ans.append(k) 
        print(ans)
        for i in range(len(nums)):
            if i+1 not in nums:
                ans.append(i+1 )
        return ans 
        
        