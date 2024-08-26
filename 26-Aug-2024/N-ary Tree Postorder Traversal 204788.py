# Problem: N-ary Tree Postorder Traversal - https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        
        if not root:
            return ans
        def recur(root):
            for i in root.children:
                recur(i)
            ans.append(root.val)
        recur(root)
        return ans
           
            

            
            
           
            