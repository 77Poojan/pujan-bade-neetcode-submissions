import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        smash = [-s for s in stones]
        heapq.heapify(smash)

        while len(smash) > 1:
            n1 = -heapq.heappop(smash)
            n2 = -heapq.heappop(smash)
            if n1 != n2:
                heapq.heappush(smash, -(n1 - n2))
        
        return -smash[0] if smash else 0
