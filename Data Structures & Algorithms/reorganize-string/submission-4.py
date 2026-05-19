from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        queue = [(-v, k) for k, v in counter.items()]
        heapq.heapify(queue)

        res = ""
        prev = None

        while queue or prev: 
            if prev and not queue:
                return ""

            v, k = heapq.heappop(queue)
            res += k
            v = v + 1

            if prev:
                heapq.heappush(queue, prev)
                prev = None

            if v != 0:
                prev = (v, k)

        return res