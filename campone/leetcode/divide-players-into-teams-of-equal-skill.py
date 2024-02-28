class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort() 
        n = len(skill)
        
        x=sum(skill) 
        temp = x * 2   
        requiredsum = temp / n  
        
        left=0
        right=len(skill)-1
        count=0
        product=[]

        while left < right :
            if skill[left] + skill[right] == requiredsum:
                
                product.append(skill[left] * skill[right])
                count+=1
                left+=1
                right-=1
                
            elif skill[left] + skill[right] < requiredsum :
                left+=1
                
            elif skill[left] + skill[right] > requiredsum :
                right-=1

        if count != n/2 :
            return -1
        
        return(sum(product))





        