/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func goodNodes(root *TreeNode) int {
    if root == nil {
        return 0
    }
    
    type pair struct {
        node *TreeNode
        maxVal int
    }

    queue := []pair{{root, math.MinInt32}}
    res := 0

    for len(queue) > 0 {
        node, maxVal := queue[0].node, queue[0].maxVal
        queue = queue[1:]

        if node.Val >= maxVal {
            res += 1
        }

		newMax := maxVal
        if node.Val > newMax {
			newMax = node.Val
		}

        if node.Left != nil { 
            queue = append(queue, pair{node.Left, newMax})
        }

        if node.Right != nil { 
            queue = append(queue, pair{node.Right, newMax})
        }
    }

    return res
}
