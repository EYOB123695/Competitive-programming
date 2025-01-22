# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        directions = [(0,-1) , (0 ,1 ) ,(1, 0) , (-1,0)]
        
        def inbound(r,c):
            return 0 <= r < len(isWater) and 0 <= c < len(isWater[0])
        height = [[0 for _ in row] for row in isWater]
        queue = deque()
        visited = set()
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    queue.append((i,j))
                    visited.add((i,j))
        val = 1
        while queue:
           
            for i in range(len(queue)) :
                r,c = queue.popleft() 
                
                for i , j in directions:
                    nr,nc = r + i ,c + j 
                    if inbound(nr,nc) and (nr,nc) not in visited:
                        queue.append((nr,nc)) 
                        visited.add((nr,nc))
                        height[nr][nc] = val 
            val +=   1 
        return height
               
        
            
        
        
                
          
        

        