func numSquares(n int) int {
    dp := make([]int, n+1)
    for i := 1; i <= n; i++ {
        dp[i] = n 
    }

    for i := 1; i <= n; i++ {
        for j := 1; j*j <= i; j++ {
            sq := j * j
            dp[i] = min(dp[i], 1 + dp[i-sq])
        }
    }

    return dp[n]
}