from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graphs = defaultdict(list)

        for u, v in prerequisites:
            graphs[u].append(v)

        UNVISITED, VISITING, VISITED = 0, 1, 2
        track = [0] * numCourses

        def dfs(node):
            if track[node] == VISITING:
                return False
            
            elif track[node] == VISITED:
                return True

            else:
                track[node] = VISITING

                for v in graphs[node]:
                    if not dfs(v):
                        return False

            track[node] = VISITED
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True