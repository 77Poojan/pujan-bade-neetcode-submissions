class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        count = 0
        w = float("inf")

        for r in range(len(nums)):
            count += nums[r]
            while count >= target:
                w = min(w, r - l + 1)
                count -= nums[l]
                l += 1

        return 0 if w == float("inf") else w