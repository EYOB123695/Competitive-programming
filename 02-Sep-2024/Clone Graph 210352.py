# Problem: Clone Graph - https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        dictionary = {}
        if not node :
            return None
        def dfs(node):
            if node in dictionary:
                return dictionary[node] 
            copy = Node(node.val)
            dictionary[node] = copy 
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy            


        return dfs(node)

        