# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashMap = {node: idx for idx, node in enumerate(inorder)}
        self.pre_idx = 0

        def construct(l, r):
            if l > r:
                return None

            root = preorder[self.pre_idx]
            self.pre_idx += 1

            node = TreeNode(root)
            mid = hashMap[root]

            node.left = construct(l, mid - 1)
            node.right = construct(mid + 1, r)

            return node

        return construct(0, len(inorder) - 1)