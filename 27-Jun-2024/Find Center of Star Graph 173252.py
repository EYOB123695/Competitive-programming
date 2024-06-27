# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dictionary = defaultdict(int)
        n = len(edges)
        for i,v in edges:
            dictionary[i] += 1 
            dictionary[v] += 1  
        for k,val in dictionary.items():
            if val == n:
                return k 
        





        