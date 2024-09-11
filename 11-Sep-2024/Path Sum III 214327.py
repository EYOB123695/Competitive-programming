# Problem: Path Sum III - https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefixsum = defaultdict(int)
        prefixsum[0] = 1 
        def dfs(root,curr):
            if not root:
                return 0
            curr += root.val 
            path = prefixsum[curr  - targetSum]
            prefixsum[curr] += 1 
            if root.left :
                path += dfs(root.left,curr)

            if root.right :
                path += dfs(root.right,curr) 
            prefixsum[curr] -= 1  
            return path 
        ans =  dfs(root,0) 
        return ans
            

        