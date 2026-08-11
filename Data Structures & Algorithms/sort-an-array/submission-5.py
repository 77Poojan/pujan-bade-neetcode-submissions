class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        count = {}
        minVal = maxVal = nums[0]

        for val in nums:
            count[val] = count.get(val, 0) + 1
            if val < minVal:
                minVal = val
            elif val > maxVal:
                maxVal = val

        index = 0
        for val in range(minVal, maxVal + 1):
            freq = count.get(val, 0)
            while freq > 0:
                nums[index] = val
                index += 1
                freq -= 1

        return nums