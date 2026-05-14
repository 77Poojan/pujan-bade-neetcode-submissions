import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.queue = nums
        self.idx = k
        heapq.heapify(self.queue)

        while len(self.queue) > self.idx:
            heapq.heappop(self.queue)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.queue, val)
        
        if len(self.queue) > self.idx:
            heapq.heappop(self.queue)

        return self.queue[0]