from collections import Counter 

class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        heap = [(-v, k) for k, v in counts.items()]
        heapq.heapify(heap)

        res = ""
        prev = None

        while heap or prev:
            ## Overlap
            if prev and not heap:
                return ""
                
            v, k = heapq.heappop(heap)
            res += k
            v = v + 1

            if prev:
                heapq.heappush(heap, prev)
                prev = None

            if v != 0:
                prev = (v, k)

        return res      