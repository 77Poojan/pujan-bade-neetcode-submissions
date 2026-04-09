class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        c = Counter(nums)
        heap, arr = [], []

        for num, freq in c.items():
            heapq.heappush(heap, (-freq, num))
        
        for _ in range(k):
            arr.append(heapq.heappop(heap)[1])
        
        return arr