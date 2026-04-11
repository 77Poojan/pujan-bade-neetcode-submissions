class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = 0
        counter = defaultdict(int)

        counter[0] = 1

        for num in nums:
            prefix += num
            res += counter[prefix - k]
            counter[prefix] += 1

        return res