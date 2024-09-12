# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i :[] for i in range(numCourses)} 
        for src,dst in prerequisites:
            graph[src].append(dst)
        visited =set()
        def dfs(i):
            if i in visited:
                return False
            if graph[i] == []:
                return True
            visited.add(i)
            for nei in graph[i]:
                if not dfs(nei):
                    return False
            visited.remove(i)
            graph[i] = []
            return True            
        for i in range(numCourses):
           if not dfs(i):
                return False
        return True


        
        