class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            nonlocal count
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                count += 1
                return
            if grid[i][j] == -1:
                return
            grid[i][j] = -1
            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                dfs(i + dx, j + dy)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return count

        return 0