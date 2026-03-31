# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if k == 0 or not root:
            return root

        self.count = k
        self.res = 0
        def dfs(root):
            if not root:
                return 

            dfs(root.left)
            self.count -= 1

            if self.count == 0:
                self.res = root.val
                return 

            dfs(root.right)
            
        dfs(root)
        return self.res