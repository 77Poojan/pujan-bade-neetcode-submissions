/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func isBalanced(root *TreeNode) bool {
    var height func(node *TreeNode) int
    height = func(node *TreeNode) int {
        if node == nil {
            return 0
        }

        left := height(node.Left)
        right := height(node.Right)

        if left == -1 || right == -1 {
            return -1
        }

        diff := left - right
        if diff < 0 {
            diff = -diff
        }
        if diff > 1 {
            return -1
        }

        if left > right {
            return 1 + left
        }
        return 1 + right
    }

    return height(root) != -1
}