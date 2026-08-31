# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        first_critical = -1
        prev_critical = -1
        min_dist = float('inf')

        prev = head
        curr = head.next
        index = 2  # 1-based index for curr

        while curr.next:
            # Check if curr is a local minimum or local maximum
            is_critical = (curr.val > prev.val and curr.val > curr.next.val) or \
                          (curr.val < prev.val and curr.val < curr.next.val)

            if is_critical:
                if first_critical == -1:
                    first_critical = index
                else:
                    min_dist = min(min_dist, index - prev_critical)
                prev_critical = index

            prev = curr
            curr = curr.next
            index += 1

        # If we found fewer than 2 critical points
        if first_critical == -1 or first_critical == prev_critical:
            return [-1, -1]

        max_dist = prev_critical - first_critical
        return [min_dist, max_dist]
        