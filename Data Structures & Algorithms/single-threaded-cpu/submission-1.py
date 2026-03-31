import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(et, pt ,idx) for idx, (et, pt) in enumerate(tasks)]
        tasks.sort()
        
        heap = []
        process_batch = []
        time, i = 0, 0
        n = len(tasks)

        while i < n or heap:
            while i < n and tasks[i][0] <= time:
                _, pt, idx = tasks[i]
                heapq.heappush(heap, (pt, idx))
                i += 1
        
            if heap:
                pt, idx = heapq.heappop(heap)
                time += pt
                process_batch.append(idx)
            else:
                time = tasks[i][0]

        return process_batch