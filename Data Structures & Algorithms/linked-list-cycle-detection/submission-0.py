# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        slower = curr
        faster = curr

        while faster and faster.next:
            slower = slower.next
            faster = faster.next.next
            if slower == faster:
                return True
 
        return False
            
        