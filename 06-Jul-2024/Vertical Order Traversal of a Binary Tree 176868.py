# Problem: Vertical Order Traversal of a Binary Tree - https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
       
        if root is None :
            return result
        dict={}
        self.minc,self.maxc=0,0
        def dfs(node,r,c):
            if node==None:
                return
            
            
            if c in dict:
                dict[c].append([r,node.val])
            else:
                dict[c]=[[r,node.val]]
            self.minc = min(self.minc,c)
            self.maxc=max(self.maxc,c)
            dfs(node.left,r+1,c-1) 
            dfs(node.right,r+1,c+1)
        dfs(root,0,0)
        for c in range(self.minc,self.maxc+1):
            col=sorted(dict[c],key=lambda x:(x[0],x[1]))
            col_sorted=[] 
            for p in col:
                col_sorted.append(p[1])
            result.append(col_sorted)
        return result
        
        