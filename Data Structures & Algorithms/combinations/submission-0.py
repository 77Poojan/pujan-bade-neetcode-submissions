class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, sol = [], []

        def backtrack(i):
            if len(sol) == k:
                res.append(sol[:])
                return

            for j in range(i, n+1):
                sol.append(j)
                backtrack(j+1)
                sol.pop()
        
        backtrack(1)
        return res