# Problem: Validate Binary Tree Nodes - https://leetcode.com/problems/validate-binary-tree-nodes/

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        visit = set()
        incoming = [0] * n
        for i in range(n):
            if leftChild[i] != -1:
                incoming[leftChild[i]] += 1
            if rightChild[i] != -1:
                incoming[rightChild[i]] += 1
        root = -1 
        for i in range(n):
            if incoming[i] == 0:
                if root == -1:
                    root = i 
                else:
                    return False
        

        arr = [True]
        def dfs(root):
            if root == -1:
                return 
            if root in visit :
                
                return 
            visit.add(root)
            dfs(leftChild[root])
            dfs(rightChild[root])
        if root == -1 :
            return False
        dfs(root)
        return len(visit) == n and sum(incoming) == n- 1
            
           
            
        

        
       

