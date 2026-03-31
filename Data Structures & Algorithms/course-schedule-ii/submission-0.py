class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        c = defaultdict(list)
        courses = prerequisites
        s = []

        for a, b in courses:
            c[a].append(b)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses

        def dfs(node):
            state = states[node]
            if state == VISITED:
                return True
            elif state == VISITING:
                return False

            states[node] = VISITING
            for n in c[node]:
                if not dfs(n):
                    return False

            states[node] = VISITED
            s.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return s