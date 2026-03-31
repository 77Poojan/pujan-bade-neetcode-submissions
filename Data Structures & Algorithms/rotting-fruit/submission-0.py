from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh, interval = 0, 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        traces = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while queue and fresh > 0:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for x, y in traces:
                    xi, yi = i + x, j + y
                    if 0 <= xi < m and 0 <= yi < n and grid[xi][yi] == 1:
                        grid[xi][yi] = 2
                        fresh -= 1
                        queue.append((xi, yi))
            interval += 1

        return -1 if fresh > 0 else interval  