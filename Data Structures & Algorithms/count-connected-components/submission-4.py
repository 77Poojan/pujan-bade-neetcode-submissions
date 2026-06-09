class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(p):
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

  
        def union(u, v):
            p1, p2 = find(u), find(v)

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
