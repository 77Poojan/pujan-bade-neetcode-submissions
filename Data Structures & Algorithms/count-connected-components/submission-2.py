class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]

        def find(p):
            p = par[p]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        rank = [1] * n
        def union(p1, p2):
            p1, p2 = find(p1), find(p2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return True
            
        res = n
        for u, v in edges:
            if union(u, v):
                res -= 1

        return res