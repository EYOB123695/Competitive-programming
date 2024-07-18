# Problem: Number of Good Leaf Nodes Pairs - https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        count = 0
        if not root:
            return 0
        
        
        
        def traverse(node,distance):
            nonlocal count
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            leftlist = traverse(node.left,distance)
            rightlist = traverse(node.right,distance)
            for i in leftlist:
                print(i)
                if i > distance:
                    continue
                for j in rightlist:
                    if i + j <= distance:
                        count +=1 
            return [k + 1 for k in leftlist+rightlist]
        traverse(root,distance)
        return count


        