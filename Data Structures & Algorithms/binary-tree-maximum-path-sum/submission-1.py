# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.summ = float("-inf")

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            leftMax = max(left, 0)
            rightMax = max(right, 0)

            current_sum = root.val + leftMax + rightMax 
            self.summ = max(self.summ, current_sum)

            return root.val + max(leftMax, rightMax)

        dfs(root)
        return self.summ