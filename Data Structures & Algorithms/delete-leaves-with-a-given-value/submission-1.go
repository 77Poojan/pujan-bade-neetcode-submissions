/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func removeLeafNodes(root *TreeNode, target int) *TreeNode {
    var check func(root *TreeNode) *TreeNode

	check = func(node *TreeNode) *TreeNode  {
		if node == nil {
			return nil
		}

		node.Left = check(node.Left)
		node.Right = check(node.Right) 

        if node.Left == nil && node.Right == nil && node.Val == target {
			return nil
		}

		return node
	}

	return check(root)
}
