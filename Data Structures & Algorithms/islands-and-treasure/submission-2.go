func islandsAndTreasure(grid [][]int) {
    if grid == nil {
        return
    }

    m := len(grid)
    n := len(grid[0])

    queue := make([][2]int, 0)

    for i := range m {
        for j := range n {
            if grid[i][j] == 0 {
                queue = append(queue, [2]int{i, j})
            }
        }
    }

    directions := [][2]int{
        {0, 1},
        {1, 0},
        {0, -1},
        {-1, 0},
    }

    for len(queue) > 0 {
        node := queue[0]
        queue = queue[1:]
        i, j := node[0], node[1]

        for _, d := range directions {
            ni, nj := i+d[0], j+d[1]
            if ni >= 0 && ni < m && nj >= 0 && nj < n && grid[ni][nj] == 2147483647 {
                grid[ni][nj] = grid[i][j] + 1
                queue = append(queue, [2]int{ni, nj})
            }
        }
    }
}
