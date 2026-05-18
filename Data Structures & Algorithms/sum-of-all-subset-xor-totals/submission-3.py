class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xor, self.curr_summ = 0, 0

        def backtrack(i, xor):
            if i == len(nums):
                self.curr_summ += xor
                return 

            backtrack(i + 1, xor)
            backtrack(i + 1, nums[i] ^ xor)
        
        backtrack(0, xor)
        return self.curr_summ