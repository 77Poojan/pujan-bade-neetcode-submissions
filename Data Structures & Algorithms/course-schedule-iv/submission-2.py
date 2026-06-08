from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for preq, crs in prerequisites:
            adj[crs].append(preq)

        def dfs(crs):
            if not crs in preq:
                preq[crs] = set()

                for p in adj[crs]: 
                    preq[crs] |= dfs(p)

                preq[crs].add(crs)
            return preq[crs]


        preq = {}
        for crs in range(numCourses):
            dfs(crs)

        res = []
        for u, v in queries:
            res.append(u in preq[v])

        return res

        