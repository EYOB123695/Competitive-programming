# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr=dummy
        temp=l1
        ptr=l2
        rem=0
        div=0
        while temp or ptr:
            x= temp.val if temp!=None else 0
            y=ptr.val if ptr!=None else 0
            s=x+y+div
            rem=s%10
            div=s//10
            curr.next=ListNode(rem)      
            if temp:
                temp=temp.next
            if ptr:
                ptr=ptr.next
            curr=curr.next
            if div>0:
                curr.next=ListNode(div)
        return dummy.next        