# Problem: Spiral Matrix IV - https://leetcode.com/problems/spiral-matrix-iv/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        result = [[-1 for _ in range(n)] for _ in range(m)]

        current = head

        top, left, right, bottom = 0, 0, n-1, m-1

        while current and left <= right and top <= bottom:

            # form left to right
            for i in range(left, right+1):
                if current:
                    result[top][i] = current.val
                    current = current.next
            
            top += 1

            # from top to bototm
            for i in range(top, bottom+1):
                if current:
                    result[i][right] = current.val
                    current = current.next
            
            right -= 1

            # form left to right
            if left <= right:
                for i in range(right, left-1, -1):
                    if current:
                        result[bottom][i] = current.val
                        current = current.next
            
            bottom -= 1

            # from bottom to top
            if top <= bottom:
                for i in range(bottom, top-1, -1):
                    if current:
                        result[i][left] = current.val
                        current = current.next
            
            left += 1
            
        return result

        
        