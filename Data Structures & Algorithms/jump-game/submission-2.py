class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        canJump = n
        i = n

        while i >= 0:
            if i + nums[i] >= canJump:
                canJump = i
            i -= 1

        return canJump == 0