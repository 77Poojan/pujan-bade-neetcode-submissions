/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

func copyRandomList(head *Node) *Node {
	if head == nil {
		return nil
	}

	hashMap := make(map[*Node]*Node)

	// First pass: create all copy nodes, mapped by original node
	curr := head
	for curr != nil {
		hashMap[curr] = &Node{Val: curr.Val}
		curr = curr.Next
	}

	// Second pass: wire up Next and Random pointers
	curr = head
	for curr != nil {
		copyNode := hashMap[curr]
		copyNode.Next = hashMap[curr.Next]     // hashMap[nil] correctly yields nil
		copyNode.Random = hashMap[curr.Random] // same here
		curr = curr.Next
	}

	return hashMap[head]
}