class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        hashMap = {
            "a": a,
            "b": b,
            "c": c
        }

        res = ""
        heap = []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(heap, (count, char))

        while heap:
            count1 , ch1 = heapq.heappop(heap)
            
            if (len(res) >= 2) and (res[-1] == res[-2] == ch1):
                if not heap:
                    break

                count2, ch2 = heapq.heappop(heap)
                res += ch2

                if count2 + 1 < 0:
                    heapq.heappush(heap, (count2 + 1, ch2))
                
                heapq.heappush(heap, (count1, ch1))

            else: 
                res += ch1
                if count1 + 1 < 0:
                    heapq.heappush(heap, (count1 + 1, ch1))

        return res