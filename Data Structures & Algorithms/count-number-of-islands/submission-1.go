func numIslands(grid [][]byte) int {
	m := len(grid)
	n := len(grid[0])
    count := 0

    traces := [][]int{
		{0, 1},
		{1, 0},
		{0, -1},
		{-1, 0},
	}

    var dfs func(x, y int) 

    dfs = func(x, y int) {
        if x < 0 || y < 0 || x >= m || y >= n || grid[x][y] == '0' {
			return 
		}
	
		grid[x][y] = '0'
        for _, value := range traces {
			xi, yj := x + value[0], y + value[1]
			dfs(xi, yj)
		}
    }


    for i := range m{
        for j := range n {
            if grid[i][j] == '1' {
                count += 1
                dfs(i, j)
            }
        }
    }

    return count
}
