/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func isValidBST(root *TreeNode) bool {
    if root == nil {
		return true
	}

	type bound struct {
		node     *TreeNode
		min, max int
	}

	queue := []bound{{root, math.MinInt64, math.MaxInt64}}

	for len(queue) > 0 {
		b := queue[0]
		queue = queue[1:]
		node := b.node

		if node.Val <= b.min || node.Val >= b.max {
			return false
		}

		if node.Left != nil {
			queue = append(queue, bound{node.Left, b.min, node.Val})
		}
		if node.Right != nil {
			queue = append(queue, bound{node.Right, node.Val, b.max})
		}
	} 

	return true
}
