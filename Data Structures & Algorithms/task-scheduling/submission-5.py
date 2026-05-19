from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        task_scheduler = [-cnt for cnt in count.values()]
        heapq.heapify(task_scheduler)

        time = 0
        cool_down_queue = deque()  # pairs of [-cnt, idleTime]

        while task_scheduler or cool_down_queue:
            time += 1
            if task_scheduler:
                cnt = 1 + heapq.heappop(task_scheduler)

                if cnt:
                    cool_down_queue.append((cnt, time + n))

            if cool_down_queue and cool_down_queue[0][1] == time:
                heapq.heappush(task_scheduler, cool_down_queue.popleft()[0])

        return time