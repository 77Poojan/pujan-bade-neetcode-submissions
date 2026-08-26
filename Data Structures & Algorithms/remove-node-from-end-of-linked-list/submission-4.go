/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func removeNthFromEnd(head *ListNode, n int) *ListNode {
    dummy := &ListNode{Next: head}
    right := dummy
    left := dummy

    for i := 0; i <= n; i++ {
        right = right.Next
    }

    for right != nil {
        left = left.Next
        right = right.Next 
    }

    left.Next= left.Next.Next

    return dummy.Next
}
