# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp= headA
        temptwo = headB 
        ans=set()

        while temp :
            ans.add(temp)
            temp=temp.next
        while temptwo :
            if temptwo in ans:
                return temptwo
            temptwo = temptwo.next
            
        return None
        
           
        