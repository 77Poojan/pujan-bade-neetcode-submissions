class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific_boundary = set()
        atlantic_boundary = set()

        grids = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(i, j, visited):
            visited.add((i, j))
            for r, c in grids:
                x, y = i + r, j + c
                if  0 <= x < m and \
                    0 <= y < n and \
                    heights[x][y] >= heights[i][j] and \
                    (x, y) not in visited:
                    dfs(x, y, visited) 
            

        for i in range(m):
            dfs(i, 0, pacific_boundary)
            dfs(i, n - 1, atlantic_boundary)
        
        for i in range(n):
            dfs(0, i, pacific_boundary)
            dfs(m - 1, i, atlantic_boundary)

        return [list(cell) for cell in (pacific_boundary & atlantic_boundary)]

        
        


        