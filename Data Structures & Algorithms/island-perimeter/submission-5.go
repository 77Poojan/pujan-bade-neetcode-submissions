func islandPerimeter(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	traces := [][]int{
		{0, 1},
		{1, 0},
		{0, -1},
		{-1, 0},
	}

	var dfs func(x, y int) int
	dfs = func(x, y int) int {
		// out of bounds or water contributes 1 edge to perimeter
		if x < 0 || y < 0 || x >= m || y >= n || grid[x][y] == 0 {
			return 1
		}
		// already visited land — contributes 0 (not water, not a new edge)
		if grid[x][y] == 2 {
			return 0
		}

		grid[x][y] = 2 // mark visited
		perimeter := 0
		for _, value := range traces {
			xi, yj := x+value[0], y+value[1]
			perimeter += dfs(xi, yj)
		}
		return perimeter
	}

	// find the first land cell to start DFS from
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				return dfs(i, j)
			}
		}
	}
	return 0
}
