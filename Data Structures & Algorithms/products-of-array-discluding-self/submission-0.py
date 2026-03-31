class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        npList = [1] * (len(nums))

        prefix = 1
        for i in  range(len(nums)):
            npList[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for j in  range(len(nums) - 1, -1, -1):
            npList[j] *= postfix 
            postfix *= nums[j]

        return npList