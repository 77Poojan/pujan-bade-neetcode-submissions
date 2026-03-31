class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.maxx = 0
        self.count = 0

        def backtrack(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return False
            
            grid[i][j] = 0
            self.count += 1
            traces = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for x, y in traces:
                xi, yi = i + x, j + y
                backtrack(xi, yi)
            return self.count

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.maxx = max(self.maxx, backtrack(i, j))
                    self.count = 0

        return self.maxx