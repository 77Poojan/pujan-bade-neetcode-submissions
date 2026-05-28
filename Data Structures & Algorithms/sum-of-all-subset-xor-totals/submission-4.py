class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xor, self.sub_sum = 0, 0

        def backtrack(i, xor):
            if i == len(nums):
                self.sub_sum += xor
                return
            
            backtrack(i + 1, xor)
            backtrack(i + 1, nums[i] ^ xor)
            return

        backtrack(0, xor)
        return self.sub_sum