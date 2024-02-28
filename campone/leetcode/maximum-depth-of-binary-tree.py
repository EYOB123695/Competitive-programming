# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans=[] 
        depthone = 0
        depthtwo = 0
        depth = 0
        def recur(root):
            if not root: 
                return 0
            
        
            
        
        
            
            a = 1 + recur(root.left)
            b =   1 + recur(root.right) 
            x = max( a, b )
            return x
        return recur(root)  
      
        


        