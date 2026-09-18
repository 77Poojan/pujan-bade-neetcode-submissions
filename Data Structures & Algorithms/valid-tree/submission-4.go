func validTree(n int, edges [][]int) bool {
    if len(edges) != (n - 1) {
        return false
    }
    
    graph := make([][] int, n)
    for _, e := range edges {
        u, v := e[0], e[1]
        graph[u] = append(graph[u], v)
        graph[v] = append(graph[v], u)
    }

    visited := make([]bool, n)
    var dfs func(node int, parent int) bool 
    count := 0

    dfs = func(node int, parent int) bool {
        if visited[node] {
            return false
        }

        visited[node] = true
        count++

        for _, v := range  graph[node] {
            if v == parent {
                continue
            }

            if !dfs(v, node) {
                return false
            }
        }
        return true
    }

    if !dfs(0, -1) {
        return false
    }

    return count == n 
}
