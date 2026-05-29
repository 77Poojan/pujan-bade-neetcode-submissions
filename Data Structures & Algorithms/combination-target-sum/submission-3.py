class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)
        s = set()

        def backtrack(i, sol, summ):
            if summ > target:
                return

            if summ == target:
                res.append(sol[:])
                return 

            for j in range(i, n):
                if summ > target:
                    return
                    
                sol.append(nums[j])
                backtrack(j, sol, summ + nums[j])
                sol.pop()
        
        backtrack(0, sol, 0)
        return res