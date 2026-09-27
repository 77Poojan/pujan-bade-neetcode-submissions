func stoneGameIII(stoneValue []int) string {
    n := len(stoneValue)
    dp := make([]int, n + 1) 

    for i := n - 1; i >= 0; i-- {
        dp[i] = math.MinInt32
        take := 0
        for j := i; j < min(i+3, n); j++ {
            take += stoneValue[j]
            dp[i] = max(dp[i], take-dp[j+1])
        }
    }

    switch {
    case dp[0] > 0:
        return "Alice"
    case dp[0] < 0:
        return "Bob"
    default:
        return "Tie"
    }
}