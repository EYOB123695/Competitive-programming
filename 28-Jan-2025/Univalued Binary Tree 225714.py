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
            return 
        else:
            node = root.val
        def check(root, node):
            if root.val != node: 
                return False 
            x= True 
            y = True
            if root.left:
                x = check(root.left,node) 
          
            if root .right:
                y = check(root.right,node)
            return x and y 
        x = check(root,node)
        return True if x != False else False
        



            

            

        
       
                

        