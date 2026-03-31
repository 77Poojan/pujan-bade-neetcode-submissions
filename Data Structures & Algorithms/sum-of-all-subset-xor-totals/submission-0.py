class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        sol, res = [], []
        n = len(nums)
        def backtrack(i):
            if i == n:
                if sol:
                    temp = sol[:]
                    for i in range(1, len(temp)):
                        temp[i] ^= temp[i-1]
                    res.append(temp[-1])
                return

            backtrack(i+1)
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

        backtrack(0)
        return sum(res)