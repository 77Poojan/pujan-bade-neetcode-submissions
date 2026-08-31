/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func maxPathSum(root *TreeNode) int {
	summ := math.MinInt32
    var check func(root *TreeNode) int

	check = func(node *TreeNode) int  {
		if node == nil {
			return 0
		}

		left := check(node.Left)
		right := check(node.Right) 
		leftMax := max(left, 0)
		rightMax := max(right, 0)

		currSum := node.Val + leftMax + rightMax
		summ = max(summ, currSum)
    
		return node.Val + max(leftMax, rightMax) 
	}

    check(root)
	return summ
}
