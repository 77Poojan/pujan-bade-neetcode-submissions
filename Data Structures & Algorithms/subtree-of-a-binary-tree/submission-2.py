# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        def subCheck(p, q):
            if not p and not q:
                return True
            
            if not p or not q or p.val != q.val:
                return False
            
            return subCheck(p.left, q.left) and subCheck(p.right, q.right)
        
        def subTraversal(root):
            if not root:
                return False
            
            if subCheck(root, subRoot):
                return True
            
            return subTraversal(root.left) or subTraversal(root.right)
        
        return subTraversal(root)