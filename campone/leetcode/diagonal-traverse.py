class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]: 
        n=len(mat)
        m=len(mat[0])
        dict=defaultdict(list)
        res=[]
        for i in range(n):
            for j in range(m):
                dict[i+j].append(mat[i][j])
        for i in range (len(dict)):
            if i % 2 == 0:
                dict[i].reverse() 
                res.extend(dict[i])
            else :
                res.extend(dict[i])
        return res
        



         
        
        
        
        
                    
                





        







        