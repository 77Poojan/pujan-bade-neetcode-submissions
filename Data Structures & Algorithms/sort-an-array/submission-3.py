class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        from collections import defaultdict

        minn, maxx = min(nums), max(nums)
        count = defaultdict(int) 

        for num in nums:
            count[num] += 1

        idx = 0
        for i in range(minn, maxx + 1):
            while count[i] > 0:
                count[i] -= 1
                nums[idx] = i
                idx += 1
        return nums