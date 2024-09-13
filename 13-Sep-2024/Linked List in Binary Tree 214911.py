# Problem: Linked List in Binary Tree - https://leetcode.com/problems/linked-list-in-binary-tree/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        tmp =  head 
        ans = [False]
        def check(node, tmp):
            if not tmp:
                return True 
            if not node or node.val != tmp.val:
                return False
            return (check(node.left,tmp.next) or check(node.right,tmp.next))
        if not root :
            return False
        if check(root,head):
            return True 
        
        return (self.isSubPath(head,root.left) or self.isSubPath(head,root.right))
          





        