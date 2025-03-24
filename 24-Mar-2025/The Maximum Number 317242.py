# Problem: The Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ans = max(nums)
      
        
       
        
        arr = set(nums)
        res = list(arr)
        
        res.sort()
        res = res [::-1]
        print(res)
        if len(res) > 2:
            return res[2]
        else:
            return ans



        