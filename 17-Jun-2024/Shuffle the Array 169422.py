# Problem: Shuffle the Array - https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        list = nums[:n]
        ans = []
        
        i = 0
        j = n
        while i < len(list) and j < len(nums):
            ans.append(list[i])
            ans.append(nums[j])
            i+=1
            j+=1
        return ans

        