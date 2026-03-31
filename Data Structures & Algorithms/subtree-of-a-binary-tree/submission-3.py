# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(p, q):
            if not p and not q:
                return True
            
            if (p and not q) or (not p and q):
                return False
            
            if p and q and p.val != q.val:
                return False
            
            return check(p.left, q.left) and check(p.right, q.right)
        
        def traverse(root):
            if not root:
                return False
 
            if check(root, subRoot):
                return True
            
            return traverse(root.left) or traverse(root.right) 

        return traverse(root)