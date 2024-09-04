# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False 
        # queue = deque([(root ,0)] )
        # print(queue)
        # while queue:
        #     val,dist = queue.popleft()
        queue = deque([(root, root.val)])
        print(queue)
        while queue:
            val, dist = queue.popleft() 
          
            if dist  == targetSum and not val.left and not val.right:
                return True

            if val.left :
                queue.append((val.left, dist + val.left.val) )
            if val.right:
                queue.append((val.right , dist + val.right.val))  
        return False








        