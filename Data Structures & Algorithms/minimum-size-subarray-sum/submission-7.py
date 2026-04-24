class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:  
        r = 0
        minn = float("inf")
        n = len(nums)

        while r < n:
            summ = 0
            l = r

            while summ < target and l < n:
                summ += nums[l]
                l += 1

            if summ >= target: minn = min(minn, l - r)
            r += 1

        return 0 if minn == float("inf") else minn