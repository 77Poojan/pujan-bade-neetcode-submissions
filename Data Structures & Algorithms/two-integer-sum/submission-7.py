class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:  
        seen = {}

        for idx, num in enumerate(nums):
            temp = target - num

            if temp in seen:
                return [seen[temp], idx]

            seen[num] = idx
        return []
