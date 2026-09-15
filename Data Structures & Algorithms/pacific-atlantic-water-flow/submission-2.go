func pacificAtlantic(heights [][]int) [][]int {
	rows, cols := len(heights), len(heights[0])
	directions := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

	pacific := make([][]bool, rows)
	atlantic := make([][]bool, rows)
	for i := range pacific {
		pacific[i] = make([]bool, cols)
		atlantic[i] = make([]bool, cols)
	}

	var dfs func(r, c int, visited [][]bool)
	dfs = func(r, c int, visited [][]bool) {
		visited[r][c] = true
		for _, d := range directions {
			x, y := r+d[0], c+d[1]
			if x >= 0 && x < rows && y >= 0 && y < cols &&
				!visited[x][y] && heights[x][y] >= heights[r][c] {
				dfs(x, y, visited)
			}
		}
	}

	for i := 0; i < rows; i++ {
		dfs(i, 0, pacific)
		dfs(i, cols-1, atlantic)
	}
	for j := 0; j < cols; j++ {
		dfs(0, j, pacific)
		dfs(rows-1, j, atlantic)
	}

	result := make([][]int, 0)
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if pacific[i][j] && atlantic[i][j] {
				result = append(result, []int{i, j})
			}
		}
	}
	return result
}
