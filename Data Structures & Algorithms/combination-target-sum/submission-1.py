class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)

        def backtrack(i, summ):
            if summ > target:
                return 
            
            if summ == target:
                res.append(sol[:])
                return 

            for j in range(i, n):
                sol.append(nums[j])
                backtrack(j, summ + nums[j])
                sol.pop()

        backtrack(0, 0)
        return res