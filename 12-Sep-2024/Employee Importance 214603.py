# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int: 
        graph =  defaultdict(list)
        ans = 0
        for i in range(len(employees)):
            graph[employees[i].id].append(employees[i].importance)
            graph[employees[i].id].append(employees[i].subordinates)
        def dfs(id):
            nonlocal ans 
            ans +=  graph[id][0]
            for j in graph[id][1]:

                dfs(j) 

        dfs(id)
        return ans


      




        