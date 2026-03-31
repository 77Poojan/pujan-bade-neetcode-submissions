class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        j = 0
        for i in range(n, 2*n):
            nums.append(nums[j])
            j += 1
        return nums
        