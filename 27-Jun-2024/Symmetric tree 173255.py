# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recur(rootone,roottwo):
            if not rootone and not roottwo:
                return True 
            if not rootone and roottwo:
                return False 
            if rootone and not roottwo:
                return False 
            if rootone.val == roottwo.val:
                if recur(rootone.left,roottwo.right):
                    if recur(roottwo.left,rootone.right):
                        return True 
            else :
                return False
                    
            
        if not root:
            return True 
        else:
            return recur(root.left,root.right)
        
       