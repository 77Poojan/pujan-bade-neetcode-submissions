class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        i, goal = n, n

        while i >= 0:
            if i + nums[i] >= goal:
                goal = i
            i -= 1
        return goal == 0