class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        edges = [[] for _ in range(n)]
        indegree = [0] * n
        for u,v in invocations:
            edges[u].append(v)
            indegree[v] += 1 
        suspicious = [0] * n 
        suspicious[k] = 1 
        queue =deque([k])
        while queue:
            u = queue.popleft()
            for v in edges[u]:
                indegree[v] -= 1
                if  suspicious[v] == 0 :
                    queue.append(v)
                    suspicious[v] = 1 
        checker = True
        for i in range(n):
            if suspicious[i] == 1 and indegree[i] > 0 :
                checker = False 
                break
        if not  checker :
            return list(range(n))
        
        return [i for i in range(n) if suspicious[i] == 0]
        



                
            






        