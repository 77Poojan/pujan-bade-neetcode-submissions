class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)

        def backtrack(i, summ):
            if summ == target:
                res.append(sol[:])
                return
                
            if summ > target or i == n:
                return
 
            backtrack(i+1, summ)

            sol.append(nums[i])
            backtrack(i, summ+nums[i])
            sol.pop()

        backtrack(0, 0)
        return res