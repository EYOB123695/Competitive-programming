# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        l = 0 
        r = len(skill)-1
        skill.sort()
        ans = []
        while l < r :
            ans.append((skill[l],skill[r]))
            sum = skill[l] + skill[r]
            l+=1 
            r-=1 
        chemistry = 0
        for i,j in ans:
            if i+j != sum:
                return -1  
            chemistry += (i*j) 
        return chemistry
           
        

        
        
        
            
        