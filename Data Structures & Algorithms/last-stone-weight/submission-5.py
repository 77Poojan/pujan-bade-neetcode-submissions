import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        smash = [-s for s in stones]
        heapq.heapify(smash)

        while len(smash) > 1:
            s1 = -heapq.heappop(smash)
            s2 = -heapq.heappop(smash)
            if s1 != s2:
                heapq.heappush(smash, -(s1 - s2))

        return -smash[0] if smash else 0
