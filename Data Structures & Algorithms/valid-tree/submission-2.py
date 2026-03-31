from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n - 1):
            return False

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        

        VISITED = set()
        def dfs(node, parent):
            if node in VISITED:
                return False

            VISITED.add(node)
            for v in graph[node]:
                if v == parent:
                    continue
                if not dfs(v, node):
                    return False
            return True

        if not dfs(0, -1):
            return False

        return len(VISITED) == len(graph)