class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dic = {0: 1}
        curr_sum = 0
        total_subarrays = 0
        
        for num in nums:
            curr_sum += num
            if curr_sum - goal in dic:
                total_subarrays += dic[curr_sum - goal]
            dic[curr_sum] = dic.get(curr_sum, 0) + 1

        return total_subarrays