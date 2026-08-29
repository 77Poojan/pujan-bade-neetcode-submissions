/**
 * Definition for a QuadTree node.
 * type Node struct {
 *     Val bool
 *     IsLeaf bool
 *     TopLeft *Node
 *     TopRight *Node
 *     BottomLeft *Node
 *     BottomRight *Node
 * }
 */

 /**
 * Definition for a QuadTree node.
 * type Node struct {
 *     Val bool
 *     IsLeaf bool
 *     TopLeft *Node
 *     TopRight *Node
 *     BottomLeft *Node
 *     BottomRight *Node
 * }
 */

func construct(grid [][]int) *Node {
	var dfs func(n, r, c int) *Node
	dfs = func(n, r, c int) *Node {
		if n == 1 {
			return &Node{Val: grid[r][c] == 1, IsLeaf: true}
		}

		mid := n / 2
		topLeft := dfs(mid, r, c)
		topRight := dfs(mid, r, c+mid)
		bottomLeft := dfs(mid, r+mid, c)
		bottomRight := dfs(mid, r+mid, c+mid)

		if topLeft.IsLeaf && topRight.IsLeaf && bottomLeft.IsLeaf && bottomRight.IsLeaf &&
			topLeft.Val == topRight.Val &&
			topRight.Val == bottomLeft.Val &&
			bottomLeft.Val == bottomRight.Val {
			return &Node{Val: topLeft.Val, IsLeaf: true}
		}

		return &Node{
			Val:         false,
			IsLeaf:      false,
			TopLeft:     topLeft,
			TopRight:    topRight,
			BottomLeft:  bottomLeft,
			BottomRight: bottomRight,
		}
	}

	return dfs(len(grid), 0, 0)
}