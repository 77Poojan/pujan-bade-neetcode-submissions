class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = nums[0]
        currMin = nums[0]
        res = nums[0]

        for num in nums[1:]:
            candidates = (currMax * num, currMin * num, num)
            currMax = max(candidates)
            currMin = min(candidates)
            res = max(res, currMax)
        return res