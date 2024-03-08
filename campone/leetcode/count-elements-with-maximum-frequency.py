class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int: 
        
        ans = 0
        dict = Counter(nums) 
        print (dict)
        maxvalue = 0
        for item,values in dict.items():
            maxvalue = max(values,maxvalue)
        print(maxvalue)
        for item,value in dict.items():
            if value == maxvalue :
                ans+=value
        return ans
            

        
        
        