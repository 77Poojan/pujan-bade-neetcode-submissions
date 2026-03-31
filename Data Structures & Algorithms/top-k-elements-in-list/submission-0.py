class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        keys_sorted = sorted(c, key=c.get, reverse=True)
        return keys_sorted[:k]