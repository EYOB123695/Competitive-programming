# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        prefixsum = [0] * (len(arr) +1)
        x = 0
        for i in range(len(arr)):
            x ^= arr[i] 
            prefixsum[i] = x  
       
        for l,r in queries:
            val = prefixsum[r] ^ prefixsum[l-1] 
            ans.append(val)
        return ans

                
        