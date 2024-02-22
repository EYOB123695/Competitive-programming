class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        
        n=len(strs)
        m=len(strs[0])
        ans=[]
        x=0
        res=[]
        
        
        for i in range(n-1):
            for j in range(m):
                if strs[i][j] > strs[i+1][j]: 
                    res.append(j)
        
        return len(set(res))       
            





                
                



        