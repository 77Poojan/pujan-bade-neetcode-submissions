class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        self.total = 0

        def backtrack(i, curr_xor):
            if i == n:
                self.total += curr_xor
                return

            # don't pick nums[i]
            backtrack(i + 1, curr_xor)

            # pick nums[i]
            backtrack(i + 1, curr_xor ^ nums[i])

        backtrack(0, 0)
        return self.total 