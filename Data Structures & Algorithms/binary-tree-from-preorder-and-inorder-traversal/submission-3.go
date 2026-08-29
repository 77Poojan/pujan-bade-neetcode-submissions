/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func buildTree(preorder []int, inorder []int) *TreeNode {
    hashMap := map[int]int{}
    idx := 0

    for i:= 0; i < len(inorder); i++ {
        hashMap[inorder[i]] = i
    }

    var construct func(l int, r int) *TreeNode 
    construct = func(l int, r int) *TreeNode {
        if l > r {
            return nil
        }

        root := preorder[idx]
        idx++

        mid := hashMap[root]
        node := &TreeNode{ Val: root}

        node.Left = construct(l, mid - 1)
        node.Right = construct(mid + 1, r)

        return node
    }

    return construct(0, len(preorder) - 1)
}

