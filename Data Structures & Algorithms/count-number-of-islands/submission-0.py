class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        self.count = 0

        def backtrack(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == "0":
                return

            grid[i][j] = "0"
            traces = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for x, y in traces:
                xi, yi = i + x, j + y
                backtrack(xi, yi)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.count += 1
                    backtrack(i, j)

        return self.count