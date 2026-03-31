class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curr_max, curr_min = 1, 1

        for n in nums:
            if n == 0:
                curr_min, curr_max = 1, 1
                res = max(res, 0)
                continue

            temp = curr_max * n
            curr_max = max(n * curr_max, n * curr_min, n)
            curr_min = min(temp, n * curr_min, n)
            res = max(res, curr_max)

        return res 