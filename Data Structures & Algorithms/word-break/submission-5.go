func wordBreak(s string, wordDict []string) bool {
    n := len(s)
    dp := make([]bool, n + 1)
    dp[n] = true

    for i := n - 1; i >= 0; i-- {
        for j := 0; j < len(wordDict); j++ {
            w := wordDict[j]
            end := i + len(w)
            if end <= n && s[i:end] == w && dp[end] {
                dp[i] = true
                break
            }
        } 
    } 

    return dp[0]
}
