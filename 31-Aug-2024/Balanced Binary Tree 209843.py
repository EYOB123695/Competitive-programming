# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recur(root):
            if not root:
                return [True,0]
            left,right = recur(root.left), recur(root.right)
            if left[0] and right[0]  and abs(left[1] - right[1]) <=1  :
                balanced = True 
            else:
                balanced = False 
            return [balanced,max(left[1] , right[1]) +1 ]
        arr = recur(root)
        return arr[0]

            

       
            
        