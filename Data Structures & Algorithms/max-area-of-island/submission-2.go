func maxAreaOfIsland(grid [][]int) int {
    m := len(grid)
	n := len(grid[0])
	maxx := 0

    traces := [][]int{
		{0, 1},
		{1, 0},
		{0, -1},
		{-1, 0},
	}

    var dfs func(x, y int) int

    dfs = func(x, y int) int {
        if x < 0 || y < 0 || x >= m || y >= n || grid[x][y] == 0 {
			return 0
		}

		if grid[x][y] == 2 {
			return 0
		}

		grid[x][y] = 2
		count := 1

        for _, value := range traces {
			xi, yj := x + value[0], y + value[1]
			count += dfs(xi, yj)
		}

		return count
    }


    for i := range m{
        for j := range n {
            if grid[i][j] == 1 {
                maxx = max(maxx, dfs(i, j))
            }
        }
    }

    return maxx
}
