# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from math import gcd

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = head.next

        while curr:
            temp = curr
            n1 = curr.val
            n2 = prev.val
            val = ListNode(gcd(n1, n2), next=curr)
            prev.next = val
            prev = temp
            curr = temp.next
        
        return head