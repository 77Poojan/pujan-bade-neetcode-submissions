func findJudge(n int, trust [][]int) int {
    delta := make([]int, n+1)

    for _, t := range trust {
        delta[t[0]]--
        delta[t[1]]++
    }

    for i := 1; i <= n; i++ {
        if delta[i] == n-1 {
            return i
        }
    }


    return -1  
}
