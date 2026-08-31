/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type Codec struct {
}

func Constructor() Codec {
    return Codec {}
}

// Serializes a tree to a single string.
func (this *Codec) serialize(root *TreeNode) string {
    res := []string{}
	queue := []*TreeNode{root}

    for len(queue) > 0 {
        node := queue[0]
        queue = queue[1:]

        if node == nil {
			res = append(res, "N")
			continue
		}

       	res = append(res, strconv.Itoa(node.Val))
		queue = append(queue, node.Left)
		queue = append(queue, node.Right)
    }

    return strings.Join(res, ",")
}

// Deserializes your encoded data to tree.
func (this *Codec) deserialize(data string) *TreeNode {
    nodes := strings.Split(data, ",")

	if nodes[0] == "N" {
		return nil
	}

	rootVal, _ := strconv.Atoi(nodes[0])
	root := &TreeNode{Val: rootVal}
	queue := []*TreeNode{root}
	index := 1
        
    for len(queue) > 0 {
        node := queue[0]
        queue = queue[1:]

        if nodes[index] != "N" {
            val, _ := strconv.Atoi(nodes[index])
			node.Left = &TreeNode{Val: val}
			queue = append(queue, node.Left)
        }

        index ++

        if nodes[index] != "N" {
            val, _ := strconv.Atoi(nodes[index])
            node.Right = &TreeNode{Val: val}
            queue = append(queue, node.Right)
        }

        index ++
    }

    return root
}
