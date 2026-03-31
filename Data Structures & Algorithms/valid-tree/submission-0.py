class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)
            for child in tree[node]:
                if child == parent:
                    continue
                if not dfs(child, node):
                    return False
            
            return True
  
        if not dfs(0, -1):
            return False

        return len(visited) == n