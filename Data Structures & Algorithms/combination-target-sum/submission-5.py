class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol, res = [], []

        def backtrack(i, summ):
            if summ == target:
                res.append(sol[:])
                return 

            for j in range(i, len(nums)):
                if summ + nums[j] > target:
                    continue
                sol.append(nums[j])
                backtrack(j, nums[j] + summ)
                sol.pop()


        backtrack(0, 0)
        return res