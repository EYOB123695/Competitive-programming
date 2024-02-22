class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        onecount=0
        for i in range(len(nums)):
            if nums[i] == 1 :
                onecount+=1
                
        
        zero=0
        dict = { }
        
        dict[0] = onecount + zero
            
        for i in range(len(nums)+1):
            dict[i] = onecount + zero 
            if i < len(nums) and nums[i] == 1:
                onecount-=1
            if i < len(nums) and nums[i] == 0:
                zero += 1 
        currmax = 1
        final=[]
        arridx=list(dict.values())
        for i in  range(len(arridx)): 
            if arridx[i] == currmax :
                final.append(i)
            if arridx[i] > currmax :
                final= [i]
                currmax = arridx[i]
        return final 


            
           
        
            
                

            

            
        
        
            

        
        
        
            

        