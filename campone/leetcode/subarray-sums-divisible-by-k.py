class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        ans = 0
        l = 0
        dict ={0:1}

        for num in nums:
            l+=num
            key=l%k

            if key in dict:
                ans+=dict[key]
                dict[key]+=1
            else:
                dict[key] =1 
        return ans            
        
        