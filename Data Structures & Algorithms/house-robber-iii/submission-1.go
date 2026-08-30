/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 
func rob(root *TreeNode) int {
	var check func(root *TreeNode) (int, int)

	check = func(node *TreeNode) (int, int) {
		if node == nil {
			return 0, 0
		}

		leftRob, leftSkip := check(node.Left)
		rightRob, rightSkip := check(node.Right)
		
		robThis := node.Val + leftSkip + rightSkip
		skipThis := max(leftRob, leftSkip) + max(rightRob, rightSkip)
		
		return robThis, skipThis
	}

	return max(check(root))
}
