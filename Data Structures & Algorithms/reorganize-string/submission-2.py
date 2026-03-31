class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        heap = [(-v, k) for k, v in c.items()]
        heapq.heapify(heap)
        
        prev_ch, prev_count = "", 0
        res = []

        while heap:
            count, ch = heapq.heappop(heap)
            res.append(ch)

            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_ch))
            
            count += 1
            prev_count, prev_ch = count, ch
        
        return "".join(res) if len(res) == len(s) else ""