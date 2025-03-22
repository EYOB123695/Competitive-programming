# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(0,1) ,(1,0 ) ,(-1,0),(0,-1)]
        def inbound(r,c):
            return 0 <= r < len(maze) and 0<= c < len(maze[0])
        queue = deque([(entrance[0] , entrance[1])]) 
        level=  0
        maze[entrance[0]][entrance[1]] = "+"
        while queue:
            x = len(queue)
            for i in range(x):
                r,c = queue.popleft() 
                for i,j in directions:
                    nr , nc = i + r , j + c 
                    if inbound(nr,nc) and maze[nr][nc] == ".":
                        
                        maze[nr][nc] = "+"
                        if nr == 0 or nr == len(maze) -1 or nc == len(maze[0]) - 1 or nc == 0:
                            return level +1
                        queue.append((nr,nc))
            level += 1 
        return -1 
        











        