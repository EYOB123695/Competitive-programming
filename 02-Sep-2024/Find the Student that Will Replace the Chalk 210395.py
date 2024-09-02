# Problem: Find the Student that Will Replace the Chalk - https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        prefixsum = [0] * len(chalk) 
        prefixsum[0] = chalk[0]
        for i in range(1,len(chalk)):
            prefixsum[i] = prefixsum[i-1] + chalk[i]
      
        val = k % prefixsum[-1]
        if val == 0 :
            return(0)  
        else:
            for idx,i in enumerate(chalk) :
                val -=  i 
                if val < 0:
                    return idx
                
        
                







        