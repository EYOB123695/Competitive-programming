# Problem: Delete Nodes And Return Forest - https://leetcode.com/problems/delete-nodes-and-return-forest/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        todel = set(to_delete)
        self.ans= [] 
        self.dfs(root,todel,True) 
        return self.ans

       
    def dfs(self,root,todel,isroot):
        if not root :
            return 
        if root.val in todel:
            self.dfs(root.left,todel,True)
            self.dfs(root.right,todel,True)
        else :
            if root.left :   
                if root.left.val in todel: 
                    self.dfs(root.left,todel,True)
                    root.left = None 
                else :
                    self.dfs(root.left,todel,False)
            if root.right: 
                if root.right.val in todel: 
                    self.dfs(root.right,todel,True)
                    root.right = None 
                else :
                    self.dfs(root.right,todel,False)


            if isroot:
              self.ans.append(root)

       


       
        