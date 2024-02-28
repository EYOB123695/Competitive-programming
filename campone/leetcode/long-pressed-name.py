class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        
        i,j=0,0
        n= len(typed)
        m =len(name)
        while j<n:
            if i<m and typed[j]==name[i]:
                j+=1
                i+=1
            elif j>0 and typed[j]==typed[j-1]:
                j+=1
            else:
                return False
        if i==m :
            return True
            
