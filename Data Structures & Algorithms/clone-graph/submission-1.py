"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        hashMap = {}
        
        def dfs(curr):
            if curr in hashMap:
                return hashMap[curr]

            nn = Node(curr.val)
            hashMap[curr] = nn

            for nei in curr.neighbors:
                nn.neighbors.append(dfs(nei))    

            return nn 

        return dfs(node) if node else None