class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        def robb(nums):
            prev, curr = nums[0], max(nums[0], nums[1])
            for i in range(2, len(nums)):
                prev, curr = curr, max(curr, nums[i] + prev)
            return curr

        return max(robb(nums[1:]), robb(nums[:-1]))