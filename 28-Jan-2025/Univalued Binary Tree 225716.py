# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(node):
            if not node :
                return True 
            if root.val != node.val: 
                return False 
            
           
            return dfs(node.left) and dfs(node.right)
        return dfs(root)
        



            

            

        
       
                

        