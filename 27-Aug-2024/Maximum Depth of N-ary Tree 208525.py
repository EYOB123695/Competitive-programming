# Problem: Maximum Depth of N-ary Tree - https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        val = -float("inf")
        count = 0
        def dfs(root,count):
            nonlocal val
            if not root.children:
                val = max(val,count)
                count-=1
            for i in root.children:
              
                dfs(i,count + 1)
            return val
        return dfs(root,0) +1







        