class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        length = 1
        freq = defaultdict(int)
        l = 0
        for i in range(len(nums)):
            freq[nums[i]] += 1
            
            # if freq[nums[i]] > k :
            #     length = max(i- l   ,length)
            while freq[nums[i]] > k:
                
                
               
                freq[nums[l]] -= 1
                l+= 1
            length = max( (i- l ) + 1,length)
        return length
            
             


        