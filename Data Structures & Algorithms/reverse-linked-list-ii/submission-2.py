# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head, left, right):
        # if not head or left == right:
        #     return head
    
        # dummy = ListNode(0)
        # dummy.next = head
        # prev = dummy

        # for _ in range(left - 1):
        #     prev = prev.next
        
        # curr = prev.next
        # for _ in range(right - left):
        #     temp = curr.next
        #     curr.next = temp.next
        #     temp.next = prev.next
        #     prev.next = temp

        # return dummy.next


        dummy = ListNode(0, head)
        leftPrev, cur = dummy, head

        for _ in range(left - 1):
            leftPrev, cur = cur, cur.next

        prev = None
        for _ in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev
            prev, cur = cur, tmpNext

        leftPrev.next.next = cur
        leftPrev.next = prev

        return dummy.next