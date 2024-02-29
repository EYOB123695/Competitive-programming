# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummynode=ListNode(0,head)
        fast = head
        slow =  dummynode
        for i in range(n):
            fast = fast.next 
        while fast :
            fast = fast.next
            slow = slow.next
             
        if not fast : 
            slow.next = slow.next.next 
        return dummynode.next 


        
        