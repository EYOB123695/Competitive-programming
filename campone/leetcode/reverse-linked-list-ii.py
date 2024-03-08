# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        lP, cur = dummy, head
        for i in range(left-1):
            lP, cur = cur, cur.next

        prev = None 
        for i in range(right-left+1):
            tmpNext = cur.next
            cur.next = prev 
            prev, cur = cur, tmpNext
        lP.next.next = cur 
        lP.next = prev 
        return dummy.next 
        