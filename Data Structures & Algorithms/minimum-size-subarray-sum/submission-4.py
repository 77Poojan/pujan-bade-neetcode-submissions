class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:  
        minn = float("inf")
        l = 0
        summ = 0
        for r in range(len(nums)):
            summ += nums[r]
            while summ >= target:
                W = r - l + 1
                minn = min(minn, W)
                summ -= nums[l]
                l += 1
            
        return 0 if minn == float("inf") else minn