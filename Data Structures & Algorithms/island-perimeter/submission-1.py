class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        def dfs(i, j):

            # Out of bounds contributes perimeter
            if i < 0 or j < 0 or i >= m or j >= n:
                return 1

            # Water contributes perimeter
            if grid[i][j] == 0:
                return 1

            # Already visited
            if grid[i][j] == -1:
                return 0

            # Mark visited
            grid[i][j] = -1

            perimeter = 0

            for dx, dy in directions:
                perimeter += dfs(i + dx, j + dy)

            return perimeter

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return dfs(i, j)

        return 0