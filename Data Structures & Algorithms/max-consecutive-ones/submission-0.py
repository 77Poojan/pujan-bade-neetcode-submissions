class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = float("-inf")
        count = 0

        for num in nums:
            if num == 0:
                maxx = max(maxx, count)
                count = 0
            else:
                count += 1 
        return max(maxx, count)