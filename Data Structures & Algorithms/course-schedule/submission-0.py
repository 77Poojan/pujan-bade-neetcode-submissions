class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        routes = defaultdict(list)
        for u, v in prerequisites:
            routes[u].append(v)

        UNVISITED, VISITING, VISITED = 0, 1, 2
        track = [UNVISITED] * numCourses

        def dfs(node):
            if track[node] == VISITING:
                return False
            elif track[node] == VISITED:
                return True

            track[node] = VISITING

            for route in routes[node]:
                if not dfs(route): 
                    return False

            track[node] = VISITED
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True