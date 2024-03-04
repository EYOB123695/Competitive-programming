# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        res=[]
        def recur(root):
            if not root:
                return
        
        
            ans.append(root.val) 
        
        
            recur(root.left)
            recur(root.right)
        recur(root)
        dict = Counter(ans)
        
        
        maximum = max(dict.values())
        
        for key,value in dict.items():
            if value == maximum:
                res.append(key)

              
            
        return res
        
                 

            


            
            
            


        

        
        
        
        
        


        