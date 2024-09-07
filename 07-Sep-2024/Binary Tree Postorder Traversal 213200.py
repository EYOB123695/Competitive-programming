# Problem: Binary Tree Postorder Traversal - https://leetcode.com/problems/binary-tree-postorder-traversal/description/

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def traverse(root):
            if not root:
                return 
            traverse(root.left)
            traverse(root.right)
            ans.append(root.val)
        traverse(root)
        return ans