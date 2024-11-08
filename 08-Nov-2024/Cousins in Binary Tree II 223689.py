# Problem: Cousins in Binary Tree II - https://leetcode.com/problems/cousins-in-binary-tree-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
        levelsum = []
        queue = deque([root])
        while queue:
            x = len(queue)
            val = 0 
            for i in range(x):
                node = queue.popleft()
                val += node.val
                if node.left: 
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right) 
            levelsum.append(val)
        
        queue = deque([(root, root.val)])
        
      
        level = 0 
        while queue:
            x = len(queue)
           
            for i in range(x):
                val,curr = queue.popleft()
                val.val = levelsum[level]- curr 
                curr= 0 
                if val.left:
                    curr += val.left.val
                if val.right:
                    curr += val.right.val
                if val.left :
                    
                    queue.append((val.left,curr))
                if val.right:
                 
                    queue.append((val.right,curr))
            level += 1 
            
        return root
            
            



            




        
        
      