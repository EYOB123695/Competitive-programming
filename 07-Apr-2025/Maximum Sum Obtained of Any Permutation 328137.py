# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

# can be solved by line sweepa as well
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        freq = [0] *(len(nums)  +1)
        for i ,j in requests : 
            freq[i] +=1 
            freq[j +1] -=1 
        for  i in range(1,len(freq)):
            freq[i] += freq[i-1]
        freq.pop()
        freq.sort(reverse = True )
        nums.sort(reverse = True)
        answer = 0 
        for f , n in zip(freq,nums):
            answer += f * n 
        return answer  % (10 ** 9 + 7 )


        
      


        
        