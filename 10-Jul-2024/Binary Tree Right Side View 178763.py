# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans  = []
        if not root:
            return ans
        queue = deque([root])
        while queue:
            n = len(queue)
           
        
            res = None
            for  i in range(n):
                v = queue.popleft()
                res = v 
                if v.left:
                    queue.append(v.left)
                if v.right:
                    queue.append(v.right) 
            if res  != None:
                ans.append(res.val) 
        return ans
        


                

        