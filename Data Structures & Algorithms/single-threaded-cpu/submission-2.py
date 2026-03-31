import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        t = [(eq, dq, idx) for idx, (eq, dq) in enumerate(tasks)]
        t.sort()

        heap, res = [], []
        i, n = 0, len(t)
        time = 0

        while i < n or heap:
            while i < n and t[i][0] <= time:
                _, dq, idx = t[i]
                heapq.heappush(heap, (dq, idx))
                i += 1

            if heap:
                dq, idx = heapq.heappop(heap)
                time += dq
                res.append(idx)
  
            else:
                time = t[i][0]

        return res