from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, t in times:
            graph[u].append((v, t))
    
        heap = [(0, k)]
        visited = set()
        max_time = 0

        while heap:
            time, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            max_time = max(max_time, time)

            for nei, t in graph[node]:
                heapq.heappush(heap, (time + t, nei))

        return max_time if len(visited) == n else -1


        

                
