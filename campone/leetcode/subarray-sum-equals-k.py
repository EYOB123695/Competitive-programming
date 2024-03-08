class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
         

        ans=0
        sum=0
        dict={0:1}
        for n in nums:
            sum+=n
            res = sum - k
            ans +=dict.get(res,0)
            dict[sum]= 1 + dict.get(sum,0)
        return ans

        
            
        


        
        