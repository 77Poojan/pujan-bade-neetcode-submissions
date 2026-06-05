from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh, minutes = 0, 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

               
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        while queue and fresh > 0:
            for i in range(len(queue)):
                i, j = queue.popleft()

                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh -= 1
                        queue.append((ni, nj))   

            minutes += 1

        return -1 if fresh > 0 else minutes
    