# Problem: Asteroid Collision - https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack  = []
       
        for i in range(len(asteroids)):
           
            while stack  and stack[-1] > 0 and asteroids[i] < 0:
                    val = stack[-1] + asteroids[i]
                    if val < 0 :
                        stack.pop()
                     
                        
                    elif val == 0 :
                        stack.pop()
                        asteroids[i] = 0 
                    else:
                        asteroids[i] = 0 

                    
                   
            
            
            if asteroids[i]:
                stack.append(asteroids[i])
               
        return stack



