from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        graph = defaultdict(list)

        for u, v in prerequisites:
            graph[u].append(v)

        UNVISITED, VISITING, VISITED = 0, 1, 2
        track = [0] * n

        def dfs(node):
            if track[node] == VISITING:
                return False
            
            elif track[node] == VISITED:
                return True

            else:
                track[node] = VISITING

                for v in graph[node]:
                    if not dfs(v):
                        return False

                track[node] = VISITED
                return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True