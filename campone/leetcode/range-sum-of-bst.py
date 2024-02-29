# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans=[]
        def recur(root):
            if not root:
                return
        
        
            ans.append(root.val) 
        
        
            recur(root.left)
            recur(root.right)
        recur(root)
        sum=0
        for i in range(len(ans)):
            if low <= ans[i] <= high:
                sum+=ans[i] 
        return sum
        

