class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMaxVal, currMinVal = 0, 0
        maxVal, minVal = nums[0], nums[0]
        total = 0

        for num in nums:
            currMaxVal = max(num, num + currMaxVal)
            currMinVal = min(num, num + currMinVal)
            total += num
            maxVal = max(maxVal, currMaxVal)
            minVal = min(minVal, currMinVal)
        
        return max(maxVal, total - minVal) if maxVal > 0 else maxVal