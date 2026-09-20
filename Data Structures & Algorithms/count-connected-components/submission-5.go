func countComponents(n int, edges [][]int) int {
    par := make([]int, n)
    rank := make([]int, n)
    for i := 0; i < n; i++ {
        par[i] = i
        rank[i] = 1
    }

    find := func(p int) int {
        for p != par[p] {
            par[p] = par[par[p]]
            p = par[p]
        }
        return p
    }

    union := func(u, v int) bool {
        p1, p2 := find(u), find(v)
        if p1 == p2 {
            return false
        }
        if rank[p1] > rank[p2] {
            par[p2] = p1
            rank[p1] += rank[p2]
        } else {
            par[p1] = p2
            rank[p2] += rank[p1]
        }
        return true
    }

    res := n
    for _, e := range edges {
        if union(e[0], e[1]) {
            res--
        }
    }
    return res
}