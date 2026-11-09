/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reorderList(head *ListNode) {
   	if head == nil || head.Next == nil {
		return
	}

	fast := head
	slow := head 

	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	dummy := slow.Next
	var prev *ListNode = nil
	slow.Next = nil

	for dummy != nil {
		temp := dummy.Next
		dummy.Next = prev
		prev = dummy
		dummy = temp
	}


	first := head
	second := prev

	for second != nil {
		temp1 := first.Next 
		temp2 := second.Next

		first.Next = second
		second.Next = temp1

		first = temp1
		second = temp2
	}
}
