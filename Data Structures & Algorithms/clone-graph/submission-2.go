/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Neighbors []*Node
 * }
 */

func cloneGraph(node *Node) *Node {
    if node == nil {
        return nil
    }

    hashMap := make(map[*Node]*Node)

    var dfs func(curr *Node) *Node
    dfs = func(curr *Node) *Node {
        if hashMap[curr] != nil {
            return hashMap[curr]
        }

        nn := &Node{Val: curr.Val}
        hashMap[curr] = nn

        for _, nei := range curr.Neighbors {
            nn.Neighbors = append(nn.Neighbors, dfs(nei))
        }

        return nn
    }

    return dfs(node)
}