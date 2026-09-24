func numDecodings(s string) int {
    dp := map[int]int{len(s): 1}

    for i := len(s) - 1; i >= 0; i-- {
        if s[i] == '0' {
            dp[i] = 0
        } else {
            dp[i] = dp[i+1]
        }

        if i+1 < len(s) {
            twoDigit := (s[i]-'0')*10 + (s[i+1] - '0')
            if twoDigit >= 10 && twoDigit <= 26 {
                dp[i] += dp[i+2]
            }
        }
    }

    return dp[0]
}