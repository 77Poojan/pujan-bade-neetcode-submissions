func numSquares(n int) int {
	dp := make([]int, n + 1)

    for i := range n + 1 {
        dp[i] = n
    }

    dp[0] = 0

	for i:= 1; i < n + 1; i++ {
		for j := 1; j < i + 1; j++ {
            sq := j * j

            if i - sq < 0 {
                break
            }

			dp[i] = min(dp[i], 1 + dp[i - sq])
		}
	}
    
    return dp[n]
}
