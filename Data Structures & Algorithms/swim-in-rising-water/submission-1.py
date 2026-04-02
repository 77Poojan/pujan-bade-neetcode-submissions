class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        traces = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = [(grid[0][0], 0, 0)]

        visited = set()
        cost, maxx = 0, 0

        while queue:
            cost, x, y = heapq.heappop(queue)

            if (x, y) in visited:
                continue

            visited.add((x, y))
            maxx = max(maxx, cost)

            if  (x, y) == (m - 1, n - 1):
                return maxx

            for i, j in traces:
                xi, yj = x + i, y + j

                if 0 > xi or xi >= m or \
                    0 > yj or yj >= n or \
                    (xi, yj) in visited:
                    continue
        
                heapq.heappush(queue, (grid[xi][yj], xi, yj))

        return maxx