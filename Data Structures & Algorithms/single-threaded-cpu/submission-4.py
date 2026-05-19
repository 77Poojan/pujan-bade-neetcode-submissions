import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted(
            [(e, p, i) for i, (e, p) in enumerate(tasks)]
        )

        heap = []
        res = []

        time = 0
        i = 0
        n = len(tasks)

        while i < n or heap:

            if not heap and time < tasks[i][0]:
                time = tasks[i][0]

            while i < n and tasks[i][0] <= time:
                _, process, idx = tasks[i]
                heapq.heappush(heap, (process, idx))
                i += 1

            process, idx = heapq.heappop(heap)

            time += process
            res.append(idx)

        return res