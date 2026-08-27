/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 
func reverseBetween(head *ListNode, left int, right int) *ListNode {
    dummy := &ListNode{Next: head}
    start := dummy

    // Move start to the node just before position `left`
    for i := 0; i < left-1; i++ {
        start = start.Next
    }

    curr := start.Next  // first node of the sublist to reverse
    var prev *ListNode = nil

    // Standard reversal of the sublist [left, right]
    for i := 0; i < right-left+1; i++ {
        temp := curr.Next
        curr.Next = prev   // <- fixed: was curr.Next = curr.Next
        prev = curr
        curr = temp
    }

    // Reconnect: start.Next was the OLD first node of the sublist,
    // which is now the TAIL of the reversed sublist — link it to what comes after
    start.Next.Next = curr

    // start.Next needs to point to the new head of the reversed sublist, which is `prev`
    start.Next = prev

    return dummy.Next
}