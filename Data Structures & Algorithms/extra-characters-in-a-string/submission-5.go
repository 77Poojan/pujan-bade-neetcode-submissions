func minExtraChar(s string, dictionary []string) int {
	wordSet := make(map[string]bool)
	for _, w := range dictionary {
		wordSet[w] = true
	}

	n := len(s)
	dp := make([]int, n+1)

	for i := n - 1; i >= 0; i-- {
		dp[i] = dp[i+1] + 1

		for j := i + 1; j <= n; j++ {
			if wordSet[s[i:j]] && dp[j] < dp[i] {
				dp[i] = dp[j]
			}
		}
	}
	return dp[0]
}