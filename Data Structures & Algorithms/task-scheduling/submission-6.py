from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        scheduler = [-c for c in counts.values()]

        heapq.heapify(scheduler)
        time = 0
        cooldown_queue = deque() 

        while cooldown_queue or scheduler:
            time += 1

            if scheduler:
                cnt = 1 + heapq.heappop(scheduler)

                if cnt:
                    cooldown_queue.append((cnt, time + n))
            
            if cooldown_queue and cooldown_queue[0][1] == time:
                heapq.heappush(scheduler, cooldown_queue.popleft()[0])
            
        return time