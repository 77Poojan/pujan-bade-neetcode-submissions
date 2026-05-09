# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True

            # Current node must be within range
            if not (low < node.val < high):
                return False

            # Left subtree: values must be < node.val
            # Right subtree: values must be > node.val
            return (
                validate(node.left, low, node.val) and
                validate(node.right, node.val, high)
            )

        return validate(root)