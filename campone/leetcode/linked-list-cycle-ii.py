# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head 
        slow = head 
        while fast and fast.next: 
            slow = slow.next  
            fast = fast.next.next  
            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        fast = head  
        while fast and slow :  
            if slow == fast :
                    return slow 
            slow = slow.next
            fast = fast.next 
        return None
        