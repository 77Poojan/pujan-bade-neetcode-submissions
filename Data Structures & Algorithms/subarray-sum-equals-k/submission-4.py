from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap = defaultdict(int)
        hashMap[0] = 1
        prefix_sum = 0
        result = 0

        for num in nums:
            prefix_sum += num
            result += hashMap[prefix_sum - k]
            hashMap[prefix_sum] += 1

        return result