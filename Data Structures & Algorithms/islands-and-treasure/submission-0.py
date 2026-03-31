class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        queue = deque()

        # Step 1: add all treasures to the queue
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j))

        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        # Step 2: BFS
        while queue:
            i, j = queue.popleft()
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 2147483647:
                    grid[ni][nj] = grid[i][j] + 1
                    queue.append((ni, nj))


        