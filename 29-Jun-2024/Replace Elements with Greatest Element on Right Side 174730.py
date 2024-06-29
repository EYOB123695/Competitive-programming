# Problem: Replace Elements with Greatest Element on Right Side - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
      
         
        ans = [0] *len(arr)
        c = -1
        for i in range(len(arr)-1,-1,-1):
            ans[i] = c
            c = max(arr[i],c)
        return ans

           


        