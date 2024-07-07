# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        r = head.next
        l = head
        count = 0
        while r != None :
            if r.val != 0: 
                count += r.val 
               
            else:
                l.next.val = count 
                count = 0 
                l = l.next 
            r = r.next
        l.next = None
        return head.next 