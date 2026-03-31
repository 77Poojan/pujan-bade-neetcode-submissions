class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(candidates)

        def backtrack(i, summ):
            if i > n or summ > target:
                return 
            
            if summ == target:
                temp = sol[:]
                temp.sort()
                if temp not in res: res.append(temp)
                return 

            for j in range(i, n):
                sol.append(candidates[j])
                backtrack(j + 1, summ + candidates[j])
                sol.pop()

        backtrack(0, 0)
        return res