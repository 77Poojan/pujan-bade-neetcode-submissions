class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, sol = [], []
        n = len(candidates)

        def backtrack(i, summ):
            if summ == target:
                res.append(sol[:])
                return 
                
            if summ > target:
                return

            for j in range(i, n):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                sol.append(candidates[j])
                backtrack(j + 1, summ + candidates[j])
                sol.pop()

        backtrack(0, 0)
        return res