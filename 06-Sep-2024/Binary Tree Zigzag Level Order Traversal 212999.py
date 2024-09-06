# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return 
        queue = deque([root])
        ans = []
        flag = False
        while queue:
            x = len(queue)
            res  = []
            for i in range(x):
                val = queue.popleft()
                res.append(val.val) 
                if val.left:
                    queue.append(val.left) 
                if val.right:
                    queue.append(val.right)
            if not flag:
                ans.append(res)
                flag = True 
            else:
                ans.append(res[::-1]) 
                flag = False
        return ans
        


                


        


        