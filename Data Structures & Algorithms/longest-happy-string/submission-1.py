class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        c = ({ "a": a, "b": b, "c": c })
        heap = [(-v, k) for k, v in c.items() if v > 0]
        heapq.heapify(heap)

        res = ""

        while heap:
            count, ch = heapq.heappop(heap)
            if len(res) > 1 and res[-1] == res[-2] == ch:
                if not heap:
                    break

                count1, ch1 = heapq.heappop(heap)
                res += ch1
                count1 += 1
                if count1 < 0:
                   heapq.heappush(heap, (count1, ch1))
            else:
                res += ch
                count += 1
            if count < 0:
                heapq.heappush(heap, (count, ch))

        return res 