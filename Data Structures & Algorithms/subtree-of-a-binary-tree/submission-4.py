# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check_sub(p, q):
            if not p and not q:
                return True

            if p and not q or q and not p:
                return False

            if p.val != q.val:
                return False

            return check_sub(p.left, q.left) and check_sub(p.right, q.right)

        def dfs(root):
            if not root:
                return False

            if check_sub(root, subRoot):
                return True
            
            return dfs(root.left) or dfs(root.right)


        return dfs(root)