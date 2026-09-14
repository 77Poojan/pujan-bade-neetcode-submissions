func orangesRotting(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	queue := [][2]int{}
	fresh, minutes := 0, 0

	for i := range m {
		for j := range n {
			switch grid[i][j] {
			case 1:
				fresh++
			case 2:
				queue = append(queue, [2]int{i, j})
			}
		}
	}

	dirs := [4][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}

	for len(queue) > 0 && fresh > 0 {
		size := len(queue)
		for k := 0; k < size; k++ {
			cell := queue[0]
			queue = queue[1:]

			for _, d := range dirs {
				ni, nj := cell[0]+d[0], cell[1]+d[1]
				if ni < 0 || ni >= m || nj < 0 || nj >= n || grid[ni][nj] != 1 {
					continue
				}
				grid[ni][nj] = 2
				fresh--
				queue = append(queue, [2]int{ni, nj})
			}
		}
		minutes++
	}

	if fresh > 0 {
		return -1
	}
	return minutes
}