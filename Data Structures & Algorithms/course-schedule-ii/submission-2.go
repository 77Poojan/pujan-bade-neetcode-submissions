func findOrder(numCourses int, prerequisites [][]int) []int {
	const (
        UNVISITED = 0
        VISITING  = 1
        VISITED   = 2
    )

    graph := make([][]int, numCourses)
    for _, p := range prerequisites {
        u, v := p[0], p[1]
        graph[u] = append(graph[u], v)
    }

    track := make([]int, numCourses)
	res := []int {}

    var dfs func(node int) bool
    dfs = func(node int) bool {
        if track[node] == VISITING {
            return false
        }
        if track[node] == VISITED {
            return true
        }

        track[node] = VISITING
        for _, pre := range graph[node] {
            if !dfs(pre) {
                return false
            }
        }
        track[node] = VISITED
		res = append(res, node)
        return true
    }

    for i := 0; i < numCourses; i++ {
        if !dfs(i) {
            return []int {}
        }
    }

    return res
}
