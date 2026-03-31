# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return []

        queue = deque()
        res = 1
        if root.left: queue.append((root.left, max(root.left.val, root.val)))
        if root.right: queue.append((root.right, max(root.right.val, root.val)))


        while queue:
            n = len(queue)

            for _ in range(n):
                node, maxx = queue.popleft()
                if node:
                    if maxx <= node.val:
                        res += 1

                    if node.left: queue.append((node.left, max(maxx, node.val)))
                    if node.right: queue.append((node.right, max(maxx, node.val)))

        return res